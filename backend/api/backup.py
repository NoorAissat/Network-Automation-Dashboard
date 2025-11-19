from fastapi import APIRouter
from backend.utils.sshClient import ssh_connect
from modules.backup import backup_configs

router = APIRouter()

@router.get("")
def backup():
    conn = ssh_connect()
    backup_dir, results = backup_configs(conn)
    conn.disconnect()
    return {
        "backup_dir": backup_dir,
        "results": results
    }
