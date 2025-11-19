import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-800 text-white px-6 py-4 flex gap-6">
      <Link to="/">Dashboard</Link>
      <Link to="/health">Health</Link>
      <Link to="/services">Services</Link>
      <Link to="/wireguard">WireGuard</Link>
      <Link to="/backups">Backups</Link>
      <Link to="/drift">Drift</Link>
    </nav>
  );
}
