/**
 * Popular Immiseration — Thread 2
 * Turchin SDT: real wage stagnation vs productivity growth
 *
 * Dual Y axis:
 *   Left  — index (productivity + compensation, 1971=100)
 *   Right — percent/count (union density, labor share, strike count)
 */

import {
  ComposedChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";
import { useThreadData } from "../../hooks/useThreadData";
import { toChartData } from "../../data/reader";
import { ThreadCard } from "../ui/ThreadCard";

const FORECAST_START_YEAR = 2025;

const INDEX_SERIES = new Set([
  "productivity_index",
  "real_compensation_index",
  "productivity_forecast",
  "compensation_forecast",
]);

function CustomTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null;
  return (
    <div className="chart-tooltip">
      <p className="chart-tooltip__year">{label}</p>
      {payload.map((entry) => (
        <p key={entry.dataKey} style={{ color: entry.color }}>
          {entry.name}: {entry.value?.toFixed(1)}
          {INDEX_SERIES.has(entry.dataKey) ? "" : "%"}
        </p>
      ))}
    </div>
  );
}

export function PopularImmiseration() {
  const { data, loading, error } = useThreadData("popular_immiseration");
  const chartData = data ? toChartData(data.observationsBySeries) : [];

  return (
    <ThreadCard
      meta={data?.meta}
      warnings={data?.warnings}
      loading={loading}
      error={error}
    >
      <ResponsiveContainer width="100%" height={420}>
        <ComposedChart
          data={chartData}
          margin={{ top: 10, right: 60, left: 10, bottom: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="#222" />
          <XAxis
            dataKey="year"
            stroke="#444"
            tick={{ fill: "#666", fontSize: 11 }}
          />

          {/* Left axis — index values */}
          <YAxis
            yAxisId="index"
            orientation="left"
            stroke="#444"
            tick={{ fill: "#666", fontSize: 11 }}
            domain={[0, 420]}
            label={{
              value: "index (1971=100)",
              angle: -90,
              position: "insideLeft",
              fill: "#444",
              fontSize: 10,
              dx: -5,
            }}
          />

          {/* Right axis — percent/count */}
          <YAxis
            yAxisId="percent"
            orientation="right"
            stroke="#444"
            tick={{ fill: "#5db85d", fontSize: 11 }}
            domain={[0, 70]}
            tickFormatter={(v) => `${v}`}
            label={{
              value: "% / count",
              angle: 90,
              position: "insideRight",
              fill: "#5db85d",
              fontSize: 10,
              dx: 15,
            }}
          />

          <Tooltip content={<CustomTooltip />} />
          <Legend wrapperStyle={{ color: "#666", fontSize: 11, paddingTop: "1rem" }} />

          <ReferenceLine
            yAxisId="index"
            x={FORECAST_START_YEAR}
            stroke="#333"
            strokeDasharray="4 4"
            label={{ value: "forecast →", fill: "#444", fontSize: 10, position: "top" }}
          />

          {data &&
            Object.values(data.series).map((s) => (
              <Line
                key={s.series_id}
                yAxisId={INDEX_SERIES.has(s.series_id) ? "index" : "percent"}
                type="monotone"
                dataKey={s.series_id}
                name={s.label}
                stroke={s.color}
                strokeWidth={s.stroke_width}
                strokeDasharray={s.stroke_style === "dashed" ? "5 5" : undefined}
                dot={false}
                activeDot={{ r: 4, strokeWidth: 0 }}
                connectNulls
              />
            ))}
        </ComposedChart>
      </ResponsiveContainer>
    </ThreadCard>
  );
}
