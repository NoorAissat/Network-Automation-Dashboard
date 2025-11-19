from fastapi import APIRouter
from backend.utils.sshClient import ssh_connect
from modules.serviceMonitor import get_service_status, get_service_info

router = APIRouter()

@router.get("")
def services():
    conn = ssh_connect()
    services = ["wg-quick@wg0", "dnsmasq", "ssh", "ufw", "systemd-networkd"]
    results = {}

    for service in services:
        status = get_service_status(conn, service)
        info = get_service_info(conn, service)
        results[service] = {
            "status": status,
            "details": info
        }

    conn.disconnect()
    return results
