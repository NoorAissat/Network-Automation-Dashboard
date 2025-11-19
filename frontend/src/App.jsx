import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Health from "./pages/Health";
import Services from "./pages/Services";
import WireGuard from "./pages/WireGuard";
import Backups from "./pages/Backups";
import Drift from "./pages/Drift";

export default function App() {
  return (
    <Router>
      <Navbar />
      <div className="p-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/health" element={<Health />} />
          <Route path="/services" element={<Services />} />
          <Route path="/wireguard" element={<WireGuard />} />
          <Route path="/backups" element={<Backups />} />
          <Route path="/drift" element={<Drift />} />
        </Routes>
      </div>
    </Router>
  );
}
