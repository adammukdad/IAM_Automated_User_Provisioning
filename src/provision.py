import csv
import datetime
import os

# Define log file path
LOG_FILE = os.path.join('..', 'logs', 'provision_run.log')

def log_event(message):
    """Append timestamped message to log file."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(f"[{timestamp}] {message}\n")

def log_separator():
    """Add a visual separator line."""
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write("=" * 80 + "\n")

def process_csv(file_path):
    counts = {"create": 0, "update": 0, "terminate": 0, "unknown": 0}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            action = row['action'].strip().lower()
            if action == 'create':
                counts['create'] += 1
                log_event(f"[CREATE] Account for {row['first_name']} {row['last_name']} ({row['email']}) — Dept: {row['department']}, Role: {row['role']}")
            elif action == 'update':
                counts['update'] += 1
                log_event(f"[UPDATE] {row['email']} — Dept: {row['department']}, Role: {row['role']}")
            elif action == 'terminate':
                counts['terminate'] += 1
                log_event(f"[TERMINATE] {row['email']} ({row['first_name']} {row['last_name']}) removed from system")
            else:
                counts['unknown'] += 1
                log_event(f"[WARN] Unknown action '{action}' for user {row['email']}")
    return counts

if __name__ == "__main__":
    data_file = os.path.join('..', 'data', 'users.csv')

    log_separator()
    log_event("[INFO] Starting automated provisioning run...")
    counts = process_csv(data_file)
    log_event("[INFO] Provisioning script completed successfully.")
    log_event(f"[SUMMARY] Created: {counts['create']} | Updated: {counts['update']} | Terminated: {counts['terminate']} | Unknown: {counts['unknown']}")
    log_separator()
