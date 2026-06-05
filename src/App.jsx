import { EliteOverproduction } from "./components/threads/EliteOverproduction";
import { PopularImmiseration } from "./components/threads/PopularImmiseration";
import {
  FiscalDecline,
  InstitutionalLegitimacy,
  TrustNetwork,
  CounterElite,
  MentalHealth,
  AILaborDisplacement,
  PlatformConcentration,
  GenerationalStress,
  MultipollarTransition,
  MeaningVacuum,
  AttentionCollapse,
  EntertainmentPipeline,
} from "./components/threads/ThreadStubs";
import "./index.css";

export default function App() {
  return (
    <div className="dashboard">
      <header className="dashboard__header">
        <h1 className="dashboard__title">Convergence Analysis</h1>
        <p className="dashboard__subtitle">
          Structural stress indicators — Turchin / Tainter / Goldstone framework
        </p>
      </header>

      <main className="dashboard__threads">
        <EliteOverproduction />
        <PopularImmiseration />
        <FiscalDecline />
        <InstitutionalLegitimacy />
        <TrustNetwork />
        <CounterElite />
        <MentalHealth />
        <AILaborDisplacement />
        <PlatformConcentration />
        <GenerationalStress />
        <MultipollarTransition />
        <MeaningVacuum />
        <AttentionCollapse />
        <EntertainmentPipeline />
      </main>
    </div>
  );
}
/* append this to src/index.css */
