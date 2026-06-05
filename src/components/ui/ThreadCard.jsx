/**
 * ThreadCard — wrapper for every thread component.
 * Handles title, staleness indicator, source attribution,
 * warnings, and loading/error states.
 */

export function ThreadCard({ meta, warnings = [], loading, error, children }) {
  if (loading) {
    return (
      <div className="thread-card thread-card--loading">
        <div className="thread-card__loading">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="thread-card thread-card--error">
        <div className="thread-card__error">⚠ {error}</div>
      </div>
    );
  }

  return (
    <div className="thread-card">
      <div className="thread-card__header">
        <div className="thread-card__title-row">
          <h2 className="thread-card__title">{meta.label}</h2>
          {meta.isStale && (
            <span className="thread-card__stale-badge">Update due</span>
          )}
        </div>
        <p className="thread-card__theory">{meta.theory_ref}</p>
        <div className="thread-card__meta-row">
          <span className="thread-card__source">Source: {meta.source}</span>
          <span className="thread-card__updated">
            Updated: {meta.last_updated}
          </span>
        </div>
      </div>

      {warnings.length > 0 && (
        <div className="thread-card__warnings">
          {warnings.map((w, i) => (
            <div key={i} className="thread-card__warning">⚠ {w}</div>
          ))}
        </div>
      )}

      <div className="thread-card__body">{children}</div>
    </div>
  );
}
