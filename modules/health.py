import re

def get_health_report(conn):

    # -------------------------------------------------
    # CPU PARSING
    # -------------------------------------------------
    cpu_raw = conn.send_command("top -bn1 | grep 'Cpu(s)'").strip()

    # Example variations:
    # Cpu(s):  0.0%us,  1.0%sy,  0.0%ni, 99.0%id,  0.0%wa, ...
    # %Cpu(s): 0.0 us, 0.0 sy, 0.0 ni, 100.0 id, 0.0 wa, ...

    cpu_numbers = re.findall(r"([\d\.]+)", cpu_raw)

    # Fallback if weird output
    if len(cpu_numbers) < 5:
        cpu_numbers += ["0"] * (5 - len(cpu_numbers))

    cpu_user = float(cpu_numbers[0])
    cpu_system = float(cpu_numbers[1])
    cpu_nice = float(cpu_numbers[2])
    cpu_idle = float(cpu_numbers[3])
    cpu_iowait = float(cpu_numbers[4]) if len(cpu_numbers) > 4 else 0.0

    cpu_total = round(cpu_user + cpu_system + cpu_nice + cpu_iowait, 2)

    # -------------------------------------------------
    # MEMORY PARSING
    # -------------------------------------------------
    mem_raw = conn.send_command("free -m").splitlines()

    # Find the line that starts with "Mem:"
    mem_line = next((line for line in mem_raw if line.lower().startswith("mem")), None)

    if mem_line:
        parts = mem_line.split()
        # Format: Mem: total used free shared buff/cache available
        mem_total = float(parts[1])
        mem_used = float(parts[2])
        mem_percent = round((mem_used / mem_total) * 100, 2)
    else:
        mem_total = mem_used = mem_percent = 0

    # -------------------------------------------------
    # DISK PARSING
    # -------------------------------------------------
    disk_raw_line = conn.send_command("df -h / | tail -1").strip()
    disk_parts = disk_raw_line.split()

    # Example:
    # /dev/sda2   284G   1.8G   268G   1%   /

    disk_total = disk_parts[1] if len(disk_parts) > 1 else "0G"
    disk_used = disk_parts[2] if len(disk_parts) > 2 else "0G"
    disk_percent = disk_parts[4] if len(disk_parts) > 4 else "0%"

    # -------------------------------------------------
    # RETURN JSON STRUCTURE
    # -------------------------------------------------
    return {
        "cpu_total": cpu_total,
        "cpu_user": cpu_user,
        "cpu_system": cpu_system,
        "cpu_iowait": cpu_iowait,
        "cpu_idle": cpu_idle,

        "memory_used": mem_used,
        "memory_total": mem_total,
        "memory_percent": mem_percent,

        "disk_used": disk_used,
        "disk_total": disk_total,
        "disk_percent": disk_percent,

        "raw": {
            "cpu": cpu_raw,
            "memory": "\n".join(mem_raw),
            "disk": disk_raw_line,
        }
    }
