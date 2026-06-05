import { EliteOverproduction } from "./components/threads/EliteOverproduction";
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
      </main>
    </div>
  );
}
