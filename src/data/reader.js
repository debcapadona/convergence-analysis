/**
 * Data access interface for Convergence Analysis.
 * Today: imports static JSON files from /data directory.
 * Future: swap getThreadData() to fetch() against an API.
 * Nothing outside this file needs to change when that happens.
 */

const FORECAST_COLORS = {
  stress: "#e05252",
  counterweight: "#52a8e0",
  reference: "#f0a500",
};

/**
 * Load a thread's data file by thread name.
 * Vite handles the static asset import at build time.
 */
export async function getThreadData(threadName) {
  try {
    const module = await import(`../../data/${threadName}.json`);
    return normalizeThreadData(module.default);
  } catch (e) {
    throw new Error(`Failed to load thread data: ${threadName} — ${e.message}`);
  }
}

/**
 * Normalize raw JSON into the shape components expect.
 * Resolves forecast colors, splits observations by series,
 * and adds a staleness flag based on next_expected_update.
 */
function normalizeThreadData(raw) {
  // resolve forecast colors from type, historical colors from series definition
  const seriesMap = Object.fromEntries(
    raw.series.map((s) => [
      s.series_id,
      {
        ...s,
        color: s.is_forecast ? FORECAST_COLORS[s.type] : s.color,
      },
    ])
  );

  // group observations by series_id
  const observationsBySeries = {};
  for (const obs of raw.observations) {
    if (!observationsBySeries[obs.series_id]) {
      observationsBySeries[obs.series_id] = [];
    }
    observationsBySeries[obs.series_id].push({
      date: obs.date,
      year: parseInt(obs.date.slice(0, 4)),
      value: obs.value,
      isProjection: obs.is_projection,
      vintage: obs.vintage,
    });
  }

  // staleness check
  const nextUpdate = raw.meta.next_expected_update;
  const isStale = nextUpdate
    ? new Date() > new Date(`${nextUpdate}-01`)
    : false;

  return {
    meta: {
      ...raw.meta,
      isStale,
    },
    series: seriesMap,
    observationsBySeries,
    warnings: raw.warnings || [],
  };
}

/**
 * Flatten observations into recharts-friendly format.
 * Returns array of { year, [series_id]: value, ... }
 * One object per year, all series on the same row.
 */
export function toChartData(observationsBySeries) {
  const yearMap = {};

  for (const [seriesId, observations] of Object.entries(observationsBySeries)) {
    for (const obs of observations) {
      if (!yearMap[obs.year]) {
        yearMap[obs.year] = { year: obs.year };
      }
      yearMap[obs.year][seriesId] = obs.value;
    }
  }

  return Object.values(yearMap).sort((a, b) => a.year - b.year);
}
