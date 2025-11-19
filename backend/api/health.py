from fastapi import APIRouter
from backend.utils.sshClient import ssh_connect
from modules.health import get_health_report


router = APIRouter()

@router.get("")
def health_check():
    conn = ssh_connect()
    report = get_health_report(conn)
    conn.disconnect()
    return report
