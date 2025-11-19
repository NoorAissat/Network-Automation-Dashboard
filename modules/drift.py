import os
import difflib
from datetime import datetime

def get_backup_dirs():
    if not os.path.exists("backups"):
        return []
    dirs = [d for d in os.listdir("backups") if os.path.isdir(os.path.join("backups", d))]
    return sorted(dirs)

def compare_files(file1, file2):
    with open(file1, "r") as f1:
        old = f1.readlines()

    with open(file2, "r") as f2:
        new = f2.readlines()

    diff = difflib.unified_diff(
        old,
        new,
        fromfile=file1,
        tofile=file2,
        lineterm=""
    )

    return list(diff)  # return list of diff lines

def detect_drift():
    dirs = get_backup_dirs()

    if len(dirs) < 2:
        return None, None, "Not enough backups to detect drift."

    prev_backup = os.path.join("backups", dirs[-2])
    latest_backup = os.path.join("backups", dirs[-1])

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"reports/drift_report_{timestamp}.md"

    with open(report_filename, "w") as report:
        report.write(f"# Configuration Drift Report\n")
        report.write(f"**Previous Backup:** `{prev_backup}`\n\n")
        report.write(f"**Latest Backup:** `{latest_backup}`\n\n")
        report.write("---\n")

        prev_files = os.listdir(prev_backup)
        latest_files = os.listdir(latest_backup)
        shared_files = set(prev_files).intersection(latest_files)

        drift_found = False

        for filename in shared_files:
            file1 = os.path.join(prev_backup, filename)
            file2 = os.path.join(latest_backup, filename)

            diff = compare_files(file1, file2)

            if len(diff) > 0:
                drift_found = True
                report.write(f"\n## Changes in `{filename}`\n")
                report.write("```diff\n")
                for line in diff:
                    report.write(line + "\n")
                report.write("```\n")

        if not drift_found:
            report.write("\nNo configuration drift detected.\n")

    return report_filename, drift_found, None
