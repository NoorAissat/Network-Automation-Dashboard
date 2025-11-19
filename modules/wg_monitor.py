import os
from datetime import datetime

def parse_wg_show(raw):
    """Parse WireGuard output into a structured dict."""

    lines = raw.splitlines()
    data = {}
    current_peer = None

    for line in lines:
        stripped = line.strip()

        # Interface
        if stripped.startswith("interface:"):
            data["interface"] = stripped.split("interface:")[1].strip()

        # Public Key
        elif stripped.startswith("public key:"):
            data["public_key"] = stripped.split("public key:")[1].strip()

        # Private Key (ignore)
        elif stripped.startswith("private key:"):
            continue

        # Listening Port
        elif stripped.startswith("listening port:"):
            data["port"] = stripped.split("listening port:")[1].strip()

        # Peer
        elif stripped.startswith("peer:"):
            current_peer = stripped.split("peer:")[1].strip()
            data[current_peer] = {}

        # Peer fields
        elif "endpoint:" in stripped and current_peer:
            data[current_peer]["endpoint"] = stripped.split("endpoint:")[1].strip()

        elif "allowed ips:" in stripped and current_peer:
            data[current_peer]["allowed_ips"] = stripped.split("allowed ips:")[1].strip()

        elif "latest handshake:" in stripped and current_peer:
            data[current_peer]["handshake"] = stripped.split("latest handshake:")[1].strip()

        elif "transfer:" in stripped and current_peer:
            data[current_peer]["transfer"] = stripped.split("transfer:")[1].strip()

    return data


def monitor_wireguard(conn):
    raw_wg = conn.send_command("sudo wg show")
    raw_service = conn.send_command("systemctl status wg-quick@wg0 --no-pager -q")

    parsed = parse_wg_show(raw_wg)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"reports/wireguard_report_{timestamp}.md"

    # FIX: encode output as UTF-8 so Windows doesn't break
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# WireGuard Status Report\n")
        f.write(f"**Generated:** {timestamp}\n\n")
        f.write("## Interface Info\n")

        f.write(f"- Interface: `{parsed.get('interface', 'unknown')}`\n")
        f.write(f"- Public Key: `{parsed.get('public_key', 'unknown')}`\n")
        f.write(f"- Port: `{parsed.get('port', 'unknown')}`\n\n")

        f.write("## Peers\n")

        for key, peer in parsed.items():
            if key in ["interface", "public_key", "port"]:
                continue

            f.write(f"### Peer `{key}`\n")
            f.write(f"- Endpoint: {peer.get('endpoint', 'N/A')}\n")
            f.write(f"- Allowed IPs: {peer.get('allowed_ips', 'N/A')}\n")
            f.write(f"- Last Handshake: {peer.get('handshake', 'N/A')}\n")
            f.write(f"- Transfer: {peer.get('transfer', 'N/A')}\n\n")

        f.write("---\n")
        f.write("## Service Status\n")
        f.write("```\n")
        f.write(raw_service)
        f.write("\n```")

    return report_file


              
