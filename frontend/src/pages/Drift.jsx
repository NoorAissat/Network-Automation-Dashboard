import { useState, useEffect } from "react";
import api from "../api/client";
import Card from "../components/Card";

export default function Drift() {
  const [data, setData] = useState(null);

  const loadDrift = async () => {
    const res = await api.get("/drift/");
    setData(res.data);
  };

  useEffect(() => {
    loadDrift();
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Config Drift</h1>

      {data ? (
        <div className="space-y-4 mt-6">
          {Object.entries(data).map(([file, diff]) => (
            <Card
              key={file}
              title={file}
              value={diff === "" ? "No changes" : "Drift detected"}
              color={diff === "" ? "green" : "red"}
              details={diff || "No differences"}
            />
          ))}
        </div>
      ) : (
        <div className="text-white">Loading...</div>
      )}
    </div>
  );
}
