/**
 * Elite Overproduction — Thread 1
 * Turchin SDT: aspirant supply vs elite opening demand
 *
 * Dual Y axis:
 *   Left  — thousands (degree counts + job openings)
 *   Right — ratio (aspirants per elite opening)
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

const RATIO_SERIES = new Set([
  "aspirant_ratio",
  "aspirant_ratio_forecast",
]);

function CustomTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null;
  return (
    <div className="chart-tooltip">
      <p className="chart-tooltip__year">{label}</p>
      {payload.map((entry) => (
        <p key={entry.dataKey} style={{ color: entry.color }}>
          {entry.name}:{" "}
          {RATIO_SERIES.has(entry.dataKey)
            ? entry.value?.toFixed(2)
            : entry.value?.toLocaleString()}
          {RATIO_SERIES.has(entry.dataKey) ? "" : "k"}
        </p>
      ))}
    </div>
  );
}

export function EliteOverproduction() {
  const { data, loading, error } = useThreadData("elite_overproduction");
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

          <YAxis
            yAxisId="thousands"
            orientation="left"
            stroke="#444"
            tick={{ fill: "#666", fontSize: 11 }}
            tickFormatter={(v) => `${(v / 1000).toFixed(1)}M`}
            domain={[0, 2800]}
            label={{
              value: "thousands",
              angle: -90,
              position: "insideLeft",
              fill: "#444",
              fontSize: 10,
              dx: -5,
            }}
          />

          <YAxis
            yAxisId="ratio"
            orientation="right"
            stroke="#444"
            tick={{ fill: "#e0a050", fontSize: 11 }}
            domain={[0, 3]}
            tickFormatter={(v) => v.toFixed(1)}
            label={{
              value: "ratio",
              angle: 90,
              position: "insideRight",
              fill: "#e0a050",
              fontSize: 10,
              dx: 15,
            }}
          />

          <Tooltip content={<CustomTooltip />} />
          <Legend wrapperStyle={{ color: "#666", fontSize: 11, paddingTop: "1rem" }} />

          <ReferenceLine
            yAxisId="thousands"
            x={FORECAST_START_YEAR}
            stroke="#333"
            strokeDasharray="4 4"
            label={{ value: "forecast →", fill: "#444", fontSize: 10, position: "top" }}
          />

          {data &&
            Object.values(data.series).map((s) => (
              <Line
                key={s.series_id}
                yAxisId={RATIO_SERIES.has(s.series_id) ? "ratio" : "thousands"}
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
