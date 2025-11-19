import { useState, useEffect } from "react";
import api from "../api/client";
import Card from "../components/Card";

export default function WireGuard() {
  const [data, setData] = useState(null);

  const fetchWG = async () => {
    const res = await api.get("/wireguard/");
    setData(res.data);
  };

  useEffect(() => {
    fetchWG();
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">WireGuard Status</h1>

      {data ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          <Card
            title="Interface"
            value={data.interface || "unknown"}
            color="green"
          />

          <Card
            title="Public Key"
            value={data.public_key || "unknown"}
            color="yellow"
          />

          <Card
            title="Last Handshake"
            value={data.handshake || "unknown"}
            color={data.handshake?.includes("ago") ? "green" : "red"}
          />

          <Card
            title="Peer Allowed IPs"
            value={data.allowed_ips || "unknown"}
            color="gray"
            details={JSON.stringify(data, null, 2)}
          />
        </div>
      ) : (
        <div className="text-white">Loading...</div>
      )}
    </div>
  );
}
