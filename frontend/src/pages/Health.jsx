import { useEffect, useState } from "react";
import api from "../api/client";
import Card from "../components/Card";

export default function Health() {
  const [data, setData] = useState(null);

  const fetchHealth = async () => {
    try {
      const res = await api.get("/health/");
      setData(res.data);
    } catch (err) {
      console.error("Health fetch error:", err);
    }
  };

  useEffect(() => {
    fetchHealth();
  }, []);

  const getColor = (val, type) => {
    if (!val) return "gray";

    const num = parseFloat(val);
    if (isNaN(num)) return "gray";

    if (num < 60) return "green";
    if (num < 85) return "yellow";
    return "red";
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">System Health</h1>

      {data ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          <Card
            title="CPU Load"
            value={`${data.cpu_total}%`}
            color={getColor(data.cpu_total, "cpu")}
            details={data.raw.cpu}
          />

          <Card
            title="Memory Usage"
            value={`${data.memory_percent}%`}
            color={getColor(data.memory_percent, "memory")}
            details={data.raw.memory}
          />

          <Card
            title="Disk Usage"
            value={data.disk_percent}
            color={getColor(parseFloat(data.disk_percent), "disk")}
            details={data.raw.disk}
          />
        </div>
      ) : (
        <div className="text-white">Loading...</div>
      )}
    </div>
  );
}
