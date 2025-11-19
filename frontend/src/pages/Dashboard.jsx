import { useEffect, useState } from "react";
import api from "../api/client";
import Card from "../components/Card";
import ResourceChart from "../components/ResourceChart";

export default function Dashboard() {
  const [health, setHealth] = useState(null);
  const [services, setServices] = useState(null);
  const [wireguard, setWireguard] = useState(null);
  const [loading, setLoading] = useState(true);

  // Live chart arrays
  const [cpuGraph, setCpuGraph] = useState([]);
  const [memGraph, setMemGraph] = useState([]);
  const [diskGraph, setDiskGraph] = useState([]);

  const loadData = async () => {
    try {
      const [healthRes, servicesRes, wgRes] = await Promise.all([
        api.get("/health"),
        api.get("/services"),
        api.get("/wireguard"),
      ]);

      const h = healthRes.data;
      setHealth(h);
      setServices(servicesRes.data);
      setWireguard(wgRes.data);

      // Add new metric samples for live charts
      setCpuGraph((prev) => [...prev.slice(-19), h.cpu_total]);
      setMemGraph((prev) => [...prev.slice(-19), h.memory_percent]);
      setDiskGraph((prev) => [
        ...prev.slice(-19),
        parseFloat(h.disk_percent.replace("%", "")),
      ]);
    } catch (err) {
      console.error("Dashboard fetch error:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  if (loading) return <div className="text-white text-xl">Loading...</div>;

  const getServiceColor = (name) => {
    const status = services?.[name]?.status;
    if (!status) return "gray";
    if (status === "active") return "green";
    if (status === "inactive") return "red";
    return "yellow";
  };

  return (
    <div>
      <h1 className="text-3xl font-bold text-white mb-6">Dashboard Overview</h1>

      {/* Top-level stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

        <Card
          title="CPU Usage"
          value={`${health.cpu_total}%`}
          color={health.cpu_total < 60 ? "green" : health.cpu_total < 85 ? "yellow" : "red"}
        />

        <Card
          title="Memory Used"
          value={`${health.memory_percent}%`}
          color={health.memory_percent < 60 ? "green" : health.memory_percent < 85 ? "yellow" : "red"}
        />

        <Card
          title="Disk Used"
          value={health.disk_percent}
          color={parseFloat(health.disk_percent) < 70 ? "green" :
                 parseFloat(health.disk_percent) < 90 ? "yellow" : "red"}
        />

        <Card
          title="WireGuard Handshake"
          value={wireguard?.handshake || "unknown"}
          color={health?.cpu_total < 80 ? "green" : "yellow"}
        />

        <Card
          title="WireGuard"
          value={services["wg-quick@wg0"]?.status || "unknown"}
          color={getServiceColor("wg-quick@wg0")}
        />

        <Card
          title="DNSMasq"
          value={services["dnsmasq"]?.status || "unknown"}
          color={getServiceColor("dnsmasq")}
        />

        <Card
          title="SSH"
          value={services["ssh"]?.status || "unknown"}
          color={getServiceColor("ssh")}
        />

        <Card
          title="Firewall (UFW)"
          value={services["ufw"]?.status || "unknown"}
          color={getServiceColor("ufw")}
        />
      </div>

      {/* Live charts */}
      <h2 className="text-2xl font-bold text-white mt-10 mb-4">Live Resource Charts</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <ResourceChart label="CPU Usage (%)" dataPoints={cpuGraph} color="#00ff00" />
        <ResourceChart label="Memory (%)" dataPoints={memGraph} color="#00aaff" />
        <ResourceChart label="Disk (%)" dataPoints={diskGraph} color="#ffaa00" />
      </div>

      {/* Full system output */}
      {health?.raw && (
        <details className="mt-10 bg-gray-900 text-white p-6 rounded-lg shadow-lg border border-gray-700">
          <summary className="cursor-pointer text-xl font-semibold">Full System Output</summary>

          <pre className="mt-4 whitespace-pre-wrap text-sm leading-relaxed">
{`
CPU RAW:
${health.raw.cpu}

MEMORY RAW:
${health.raw.memory}

DISK RAW:
${health.raw.disk}
`}
          </pre>
        </details>
      )}
    </div>
  );
}


