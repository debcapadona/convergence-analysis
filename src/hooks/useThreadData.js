/**
 * Hook for loading thread data.
 * Handles loading/error states so components stay clean.
 * Usage: const { data, loading, error } = useThreadData('elite_overproduction')
 */

import { useState, useEffect } from "react";
import { getThreadData } from "../data/reader";

export function useThreadData(threadName) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      try {
        setLoading(true);
        setError(null);
        const result = await getThreadData(threadName);
        if (!cancelled) setData(result);
      } catch (e) {
        if (!cancelled) setError(e.message);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    load();
    return () => { cancelled = true; };
  }, [threadName]);

  return { data, loading, error };
}
