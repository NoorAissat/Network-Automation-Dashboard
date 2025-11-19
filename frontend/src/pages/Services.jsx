import { useState, useEffect } from "react";
import api from "../api/client";
import Card from "../components/Card";

export default function Services() {
  const [data, setData] = useState(null);

  const fetchServices = async () => {
    const res = await api.get("/services/");
    setData(res.data);
  };

  useEffect(() => {
    fetchServices();
  }, []);

  const color = status =>
    status === "active"
      ? "green"
      : status === "inactive"
      ? "red"
      : "yellow";

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Service Status</h1>

      {data ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          {Object.entries(data).map(([name, info]) => (
            <Card
              key={name}
              title={name}
              value={info.status}
              color={color(info.status)}
              details={JSON.stringify(info, null, 2)}
            />
          ))}
        </div>
      ) : (
        <div className="text-white">Loading...</div>
      )}
    </div>
  );
}
