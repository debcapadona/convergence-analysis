// ============================================================
// STUB COMPONENTS — Threads 3-14
// Each renders a ThreadCard with a "coming soon" placeholder
// until the fetcher and data file exist.
// Replace the placeholder body with a real chart as each
// fetcher is built and data/threadname.json exists.
// ============================================================

import { ThreadCard } from "../ui/ThreadCard";

function StubChart({ threadName }) {
  return (
    <div className="stub-chart">
      <p className="stub-chart__label">
        Data pipeline not yet connected — run fetchers/{threadName}.py to populate
      </p>
    </div>
  );
}

// Thread 3
export function FiscalDecline() {
  const meta = {
    label: "Fiscal State Decline",
    theory_ref: "Turchin SDT — debt service crowding out state capacity; Tainter complexity cost inflection",
    source: "OMB Historical Tables + CBO Budget Outlook",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="fiscal_decline" />
    </ThreadCard>
  );
}

// Thread 4
export function InstitutionalLegitimacy() {
  const meta = {
    label: "Institutional Legitimacy Erosion",
    theory_ref: "Goldstone — declining trust in state institutions as precursor to political crisis",
    source: "Gallup Trust in Institutions Survey 1973+",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="institutional_legitimacy" />
    </ThreadCard>
  );
}

// Thread 5
export function TrustNetwork() {
  const meta = {
    label: "Trust Network Collapse",
    theory_ref: "Putnam social capital decay — interpersonal trust as system cohesion proxy",
    source: "GSS General Social Survey 1972+",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="trust_network" />
    </ThreadCard>
  );
}

// Thread 6
export function CounterElite() {
  const meta = {
    label: "Counter-Elite Formation",
    theory_ref: "Turchin — self-funded outsider candidates as proxy for elite fragmentation",
    source: "FEC Bulk Data API",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="counter_elite" />
    </ThreadCard>
  );
}

// Thread 7
export function MentalHealth() {
  const meta = {
    label: "Mental Health Deterioration",
    theory_ref: "Popular immiseration signal — psychological stress as leading indicator of social instability",
    source: "SAMHSA National Survey on Drug Use and Health",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="mental_health" />
    </ThreadCard>
  );
}

// Thread 8
export function AILaborDisplacement() {
  const meta = {
    label: "AI Labor Displacement",
    theory_ref: "Structural unemployment driving immiseration — technology-accelerated elite overproduction pressure",
    source: "BLS Occupational Projections — decision pending",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="ai_labor_displacement" />
    </ThreadCard>
  );
}

// Thread 9
export function PlatformConcentration() {
  const meta = {
    label: "Platform Concentration",
    theory_ref: "Extraction concentration — platform monopoly as proxy for elite capture of information infrastructure",
    source: "FTC filings — free alternative to Statista TBD",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="platform_concentration" />
    </ThreadCard>
  );
}

// Thread 10
export function GenerationalStress() {
  const meta = {
    label: "Generational Stress",
    theory_ref: "Wealth cohort divergence — intergenerational mobility collapse as immiseration accelerant",
    source: "Federal Reserve Survey of Consumer Finances (triennial)",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="generational_stress" />
    </ThreadCard>
  );
}

// Thread 11
export function MultipollarTransition() {
  const meta = {
    label: "Multipolar Transition",
    theory_ref: "Fiscal state decline accelerant — dollar reserve share erosion as state capacity constraint",
    source: "IMF COFER Quarterly",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="multipolar_transition" />
    </ThreadCard>
  );
}

// Thread 12
export function MeaningVacuum() {
  const meta = {
    label: "Meaning / Religion Vacuum",
    theory_ref: "Trust network collapse accelerant — institutional meaning decline as social cohesion proxy",
    source: "Pew Research Religious Landscape Study",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="meaning_vacuum" />
    </ThreadCard>
  );
}

// Thread 13
export function AttentionCollapse() {
  const meta = {
    label: "Attention Collapse",
    theory_ref: "Social cohesion proxy — declining collective attention span as counter-deliberation signal",
    source: "Google Trends + social content half-life proxies — methodology TBD",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="attention_collapse" />
    </ThreadCard>
  );
}

// Thread 14
export function EntertainmentPipeline() {
  const meta = {
    label: "Entertainment Pipeline",
    theory_ref: "Civic participation displacement — screen time crowding out collective action capacity",
    source: "Screen time + civic participation proxies — methodology TBD",
    last_updated: "—",
    isStale: false,
  };
  return (
    <ThreadCard meta={meta} loading={false} error={null}>
      <StubChart threadName="entertainment_pipeline" />
    </ThreadCard>
  );
}
