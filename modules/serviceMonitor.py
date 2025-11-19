import os
from datetime import datetime

SERVICES = [
    "wg-quick@wg0",
    "dnsmasq",
    "ssh",
    "ufw",
    "systemd-networkd"
]

def get_service_status(conn, service):
    """Return the 'active' status from systemctl."""
    output = conn.send_command(f"systemctl is-active {service}")
    return output.strip()

def get_service_info(conn, service):
    """Return full systemctl status for the report."""
    output = conn.send_command(f"systemctl status {service} --no-pager -q")
    return output

def monitor_services(conn):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"reports/service_report_{timestamp}.md"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Service Status Report\n")
        f.write(f"**Generated:** {timestamp}\n\n")
        f.write("---\n")

        for service in SERVICES:
            status = get_service_status(conn, service)
            full_info = get_service_info(conn, service)

            f.write(f"## {service}\n")
            f.write(f"- Status: **{status}**\n\n")
            f.write("```\n")
            f.write(full_info)
            f.write("\n```\n\n")

    return report_file

