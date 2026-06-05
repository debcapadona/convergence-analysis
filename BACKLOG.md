# Convergence Analysis — Backlog

Last updated: 2026-06-04

---

## Done

- [x] Repo scaffold — directory structure, .gitignore, README
- [x] Python environment — uv, pyproject.toml, dependencies
- [x] `scripts/validate_schema.py` — JSON schema validator + cross-reference checks
- [x] `fetchers/base_fetcher.py` — base class with retry logic, logging, validate-and-write contract
- [x] `fetchers/elite_overproduction.py` — Thread 1, 141 observations, passing validation
- [x] `fetchers/popular_immiseration.py` — Thread 2, 324 observations, passing validation
- [x] Vite/React frontend initialized
- [x] `src/data/reader.js` — data interface (JSON today, API-swappable later)
- [x] `src/hooks/useThreadData.js` — data loading hook
- [x] `src/components/ui/ThreadCard.jsx` — wrapper with meta, staleness, warnings
- [x] `src/components/threads/EliteOverproduction.jsx` — dual Y axis chart rendering
- [x] `src/index.css` — dark dashboard styles
- [x] `src/App.jsx` — dashboard shell
- [x] All of the above committed and pushed to GitHub

---

## In Progress

- [ ] `src/components/threads/PopularImmiseration.jsx` — data file exists, component not written yet
- [ ] Wire PopularImmiseration into App.jsx

---

## Fetchers — Remaining 12 Threads

### Clean data, build next
- [ ] Thread 3: Fiscal State Decline — `fetchers/fiscal_decline.py`
  - FRED API (live): debt/GDP, net interest % revenue, mandatory spending %
  - Counterweight: revenue % GDP, real GDP growth
  - Update: annual (CBO Feb/March)

- [ ] Thread 4: Institutional Legitimacy — `fetchers/institutional_legitimacy.py`
  - Gallup trust indices 1973+ (hardcoded from published surveys)
  - Counterweight: civic participation proxies
  - Update: annual

- [ ] Thread 5: Trust Network Collapse — `fetchers/trust_network.py`
  - GSS interpersonal trust, biennial 50yr run (hardcoded)
  - Counterweight: social connectedness proxies
  - Update: biennial

- [ ] Thread 6: Counter-Elite Formation — `fetchers/counter_elite.py`
  - FEC self-funded candidate data (FEC bulk API — live)
  - Turchin's own proxy variable
  - Update: election cycle

- [ ] Thread 7: Mental Health — `fetchers/mental_health.py`
  - SAMHSA annual prevalence (hardcoded)
  - Counterweight: treatment access rates
  - Update: annual

### Needs API or paid data
- [ ] Thread 8: AI Labor Displacement — `fetchers/ai_labor_displacement.py`
  - Job postings YoY by category (Indeed/LinkedIn — may need proxy)
  - Decision needed: find free proxy or use BLS occupational projections instead

- [ ] Thread 9: Platform Concentration — `fetchers/platform_concentration.py`
  - Market share data (Statista paywalled — find free alternative)
  - Decision needed: use web search proxy or FTC filing data

### Needs proxy work
- [ ] Thread 10: Generational Stress — `fetchers/generational_stress.py`
  - Fed SCF median wealth by cohort (triennial — FRED API)
  - Update: triennial

- [ ] Thread 11: Multipolar Transition — `fetchers/multipolar_transition.py`
  - IMF COFER dollar reserve share (quarterly download)
  - Counterweight: USD trade settlement share
  - Update: quarterly

- [ ] Thread 12: Meaning/Religion Vacuum — `fetchers/meaning_vacuum.py`
  - Pew religious affiliation (periodic — hardcoded)
  - Counterweight: community org membership
  - Update: periodic (~4yr)

- [ ] Thread 13: Attention Collapse — `fetchers/attention_collapse.py`
  - Google Trends + social content half-life (proxies)
  - Decision needed: define proxy methodology

- [ ] Thread 14: Entertainment Pipeline — `fetchers/entertainment_pipeline.py`
  - Screen time vs civic participation (proxy-heavy)
  - Decision needed: define proxy methodology

### External feed
- [ ] Thread 15: Infrastructure Decay — fed from RidgeWatch project
  - Separate repo, separate lifecycle
  - Decision needed: how/when to wire the feed

---

## Frontend — Remaining Components

- [ ] `PopularImmiseration.jsx` — dual Y axis (index left, percent/count right)
- [ ] `FiscalDecline.jsx`
- [ ] `InstitutionalLegitimacy.jsx`
- [ ] `TrustNetwork.jsx`
- [ ] `CounterElite.jsx`
- [ ] `MentalHealth.jsx`
- [ ] `AILaborDisplacement.jsx`
- [ ] `PlatformConcentration.jsx`
- [ ] `GenerationalStress.jsx`
- [ ] `MultipollarTransition.jsx`
- [ ] `MeaningVacuum.jsx`
- [ ] `AttentionCollapse.jsx`
- [ ] `EntertainmentPipeline.jsx`
- [ ] Wire all threads into App.jsx

---

## GitHub Actions — Scheduling

- [ ] `.github/workflows/update_elite_overproduction.yml` — trigger: annual, December
- [ ] `.github/workflows/update_popular_immiseration.yml` — trigger: annual, January
- [ ] `.github/workflows/update_fiscal_decline.yml` — trigger: annual, March (CBO release)
- [ ] `.github/workflows/update_counter_elite.yml` — trigger: post-election cycle
- [ ] `.github/workflows/update_multipolar_transition.yml` — trigger: quarterly
- [ ] `.github/workflows/update_all.yml` — trigger: manual dispatch
- [ ] Add GITHUB_TOKEN permissions for committing data files back to repo

---

## GitHub Pages — Deployment

- [ ] Add `vite.config.js` base path for GitHub Pages
- [ ] `.github/workflows/deploy.yml` — build and deploy to gh-pages branch on push to main
- [ ] Verify routing works on Pages (static, no server)

---

## Future / Nice to Have

- [ ] Composite PSI score — roll up all threads into single Turchin Political Stress Index
- [ ] Thread navigation / filtering UI
- [ ] Mobile responsive layout
- [ ] Postgres swap-in — replace JSON reader with API layer
- [ ] Historical collective view — vintage comparison across time
- [ ] Dark/light mode toggle
- [ ] About/methodology page explaining the theoretical framework
- [ ] RidgeWatch feed integration (Thread 15)

---

## Decisions Needed

- Thread 8 (AI Labor Displacement): free data proxy vs BLS occupational projections
- Thread 9 (Platform Concentration): free alternative to Statista
- Threads 13/14: define proxy methodology before building
- Thread 15: RidgeWatch integration timing and mechanism

