import os
from datetime import datetime

# List of files to back up from the remote server
FILES_TO_BACKUP = [
    "/etc/network/interfaces",
    "/etc/wireguard/wg0.conf",
    "/etc/dnsmasq.conf",
    "/etc/ssh/sshd_config",
    "/etc/hosts",
    "/etc/resolv.conf",
    "/etc/fstab",
    "/etc/ufw/ufw.conf"
]

def backup_configs(conn):
    # Create timestamped folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = f"backups/{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)

    results = {}

    for file_path in FILES_TO_BACKUP:
        try:
            if file_path == "/etc/wireguard/wg0.conf":
                raw = conn.send_command("sudo cat /etc/wireguard/wg0.conf")
    
            # Remove the private key line
                output = "\n".join(
                    line for line in raw.splitlines()
                    if not line.strip().startswith("PrivateKey =")
                )


            local_filename = os.path.join(
                backup_dir,
                os.path.basename(file_path)
            )

            with open(local_filename, "w") as f:
                f.write(output)

            results[file_path] = "OK"

        except Exception as e:
            results[file_path] = f"Failed: {e}"

    return backup_dir, results
