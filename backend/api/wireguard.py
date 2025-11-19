from fastapi import APIRouter
from backend.utils.sshClient import ssh_connect
from modules.wg_monitor import parse_wg_show

router = APIRouter()

@router.get("")
def wireguard():
    conn = ssh_connect()
    raw = conn.send_command("sudo wg show")
    parsed = parse_wg_show(raw)
    conn.disconnect()
    return parsed
