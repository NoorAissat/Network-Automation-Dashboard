import { useState, useEffect } from "react";
import api from "../api/client";
import Card from "../components/Card";

export default function Backups() {
  const [data, setData] = useState(null);

  const loadBackup = async () => {
    try {
      const res = await api.get("/backup/");
      setData(res.data);
    } catch (err) {
      console.error("Backup fetch error:", err);
    }
  };

  useEffect(() => {
    loadBackup();
  }, []);

  const getColor = (val) => {
    if (typeof val === "string" && val.includes("OK")) return "green";
    return "red";
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Backup Status</h1>

      {data ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          {Object.entries(data).map(([file, result]) => (
            <Card
              key={file}
              title={file}
              value={typeof result === "string" ? result : JSON.stringify(result)}
              color={getColor(result)}
              details={JSON.stringify({ file, result }, null, 2)}
            />
          ))}
        </div>
      ) : (
        <div className="text-white">Loading...</div>
      )}
    </div>
  );
}

