# Network Automation Dashboard  
Python (FastAPI) · React · Tailwind CSS · SSH Automation · Linux · WireGuard

A full-stack network automation and monitoring platform that collects real-time system telemetry, displays service health, retrieves WireGuard VPN status, backs up configuration files, and detects configuration drift across a Linux server.

This project was created to give me a simple and reliable way to monitor my WireGuard VPN server and view real-time system information from my main PC, while also helping me learn more about networking, automation, and backend development.

---

## Features

### **1. Real-Time System Health Monitoring**
- Collects CPU, memory, and disk metrics via SSH
- Parses Linux commands like `top`, `free`, and `df -h`
- Normalizes raw data and displays it in structured UI cards

### **2. Service Status Monitoring**
- Automatically checks services such as:
  - `ssh`
  - `dnsmasq`
  - `ufw`
  - `wg-quick@wg0`
- Color-coded cards (green/yellow/red) reflect service health

### **3. WireGuard VPN Status**
- Retrieves latest handshake timestamp
- Displays whether the tunnel is active or stale
- Uses secure SSH command execution to gather real data

### **4. Automated Configuration Backups**
- Backs up key network + system files:
  - `/etc/network/interfaces`
  - `/etc/wireguard/wg0.conf`
  - `/etc/dnsmasq.conf`
  - `/etc/ssh/sshd_config`
  - `/etc/fstab`, `/etc/hosts`
- Provides pass/fail results per file in UI cards

### **5. Configuration Drift Detection**
- Compares current server configs to saved local baselines
- Highlights changed, removed, or new configuration lines
- Helps detect unintended modifications quickly

---

## Tech Stack

### **Backend**
- Python
- FastAPI
- Paramiko (SSH client)
- Linux command parsing

### **Frontend**
- React
- Vite
- Tailwind CSS

### **Infrastructure**
- WireGuard
- Linux (Debian)
- SSH-based remote command execution



