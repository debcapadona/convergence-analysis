"""
Schema definition and validator for Convergence Analysis data files.
Every fetcher calls validate_and_write() instead of writing JSON directly.
This is the contract. If it breaks here, it breaks loud before bad data lands.
"""

import json
import jsonschema
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path(__file__).parent.parent / "data"

THREAD_SCHEMA = {
    "type": "object",
    "required": ["meta", "series", "observations"],
    "properties": {
        "meta": {
            "type": "object",
            "required": [
                "thread",
                "label", 
                "last_updated",
                "update_frequency",
                "next_expected_update",
                "source",
                "theory_ref"
            ],
            "properties": {
                "thread":                {"type": "string"},
                "label":                 {"type": "string"},
                "last_updated":          {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                "update_frequency":      {"type": "string", "enum": ["daily", "monthly", "quarterly", "annual", "biennial", "periodic"]},
                "next_expected_update":  {"type": "string", "pattern": "^\\d{4}-(0[1-9]|1[0-2])$"},
                "source":                {"type": "string"},
                "theory_ref":            {"type": "string"}
            },
            "additionalProperties": False
        },
        "series": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "series_id",
                    "label",
                    "type",
                    "unit",
                    "color",
                    "stroke_style",
                    "stroke_width",
                    "is_forecast"
                ],
                "properties": {
                    "series_id":    {"type": "string"},
                    "label":        {"type": "string"},
                    "type":         {"type": "string", "enum": ["stress", "counterweight", "reference"]},
                    "unit":         {"type": "string"},
                    "color":        {"type": ["string", "null"]},
                    "stroke_style": {"type": "string", "enum": ["solid", "dashed"]},
                    "stroke_width": {"type": "number"},
                    "is_forecast":  {"type": "boolean"}
                },
                "additionalProperties": False
            }
        },
        "observations": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "date",
                    "series_id",
                    "value",
                    "is_projection",
                    "vintage",
                    "source_version"
                ],
                "properties": {
                    "date":           {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "series_id":      {"type": "string"},
                    "value":          {"type": ["number", "null"]},
                    "is_projection":  {"type": "boolean"},
                    "vintage":        {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                    "source_version": {"type": "string"}
                },
                "additionalProperties": False
            }
        },
        "warnings": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "additionalProperties": False
}


def validate(data: dict) -> list[str]:
    """
    Validate data against schema.
    Returns list of error strings — empty list means valid.
    """
    errors = []
    try:
        jsonschema.validate(instance=data, schema=THREAD_SCHEMA)
    except jsonschema.ValidationError as e:
        errors.append(f"Schema violation: {e.message} at {list(e.path)}")
    except jsonschema.SchemaError as e:
        errors.append(f"Schema definition error: {e.message}")

    # cross-reference check — every observation series_id must exist in series
    if "series" in data and "observations" in data:
        series_ids = {s["series_id"] for s in data["series"]}
        for obs in data["observations"]:
            if obs.get("series_id") not in series_ids:
                errors.append(
                    f"Observation references unknown series_id: {obs.get('series_id')}"
                )

    return errors


def validate_and_write(data: dict, thread_name: str) -> None:
    """
    Validate then write. Hard fail on schema errors. 
    Soft warn on data anomalies — those go into data['warnings'].
    Old file is never touched if validation fails.
    """
    errors = validate(data)
    if errors:
        raise ValueError(
            f"Validation failed for {thread_name}:\n" + "\n".join(errors)
        )

    # stamp the write time
    data["meta"]["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    out_path = DATA_DIR / f"{thread_name}.json"
    out_path.write_text(json.dumps(data, indent=2))
    print(f"✓ {thread_name}.json written ({len(data['observations'])} observations)")


if __name__ == "__main__":
    # run directly to validate all existing data files
    files = list(DATA_DIR.glob("*.json"))
    if not files:
        print("No data files found.")
    else:
        all_good = True
        for f in files:
            data = json.loads(f.read_text())
            errors = validate(data)
            if errors:
                print(f"✗ {f.name}:")
                for e in errors:
                    print(f"  {e}")
                all_good = False
            else:
                print(f"✓ {f.name} valid")
        if all_good:
            print("\nAll files valid.")
