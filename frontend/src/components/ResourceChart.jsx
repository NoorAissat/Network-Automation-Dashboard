import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
  Tooltip,
  Legend
);

export default function ResourceChart({ label, dataPoints, color }) {

  const data = {
    labels: dataPoints.map((_, i) => i + 1),
    datasets: [
      {
        label: label,
        data: dataPoints,
        fill: true,
        backgroundColor: `${color}33`, 
        borderColor: color,
        borderWidth: 2,
        pointRadius: 0,
        tension: 0.3,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: {
      y: {
        ticks: { color: "#ffffff" },
        grid: { color: "#444" },
      },
      x: {
        ticks: { color: "#ffffff" },
        grid: { display: false },
      },
    },
  };

  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700">
      <h2 className="text-lg font-bold text-white mb-2">{label}</h2>
      <Line data={data} options={options} />
    </div>
  );
}
