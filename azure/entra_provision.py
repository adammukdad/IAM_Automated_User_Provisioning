import json
import datetime
import os
import csv

# ---------------------------------------------------------------------
#  Microsoft Entra ID (Azure AD) Simulation Module
# ---------------------------------------------------------------------
#  This file extends your IAM automation project with an optional
#  cloud integration layer. All operations are simulated locally to
#  demonstrate workflow logic without requiring Microsoft sign-in.
# ---------------------------------------------------------------------

LOG_FILE = os.path.join('..', 'logs', 'provision_run.log')

def log_event(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(f"[{timestamp}] [AZURE] {message}\n")

def simulate_azure_call(user, action):
    """Simulate Microsoft Graph API provisioning actions."""
    log_event(f"Simulating Azure Entra ID '{action}' action for {user['email']}...")
    if action == 'create':
        log_event(f"Would create user {user['first_name']} {user['last_name']} in Entra ID.")
    elif action == 'update':
        log_event(f"Would update user {user['email']} (role={user['role']}, dept={user['department']}).")
    elif action == 'terminate':
        log_event(f"Would disable user {user['email']} in Entra ID.")
    else:
        log_event(f"Unknown action '{action}' for user {user['email']}.")

def process_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            simulate_azure_call(row, row['action'].strip().lower())

if __name__ == '__main__':
    data_file = os.path.join('..', 'data', 'users.csv')
    log_event("Starting Azure Entra ID simulation...")
    process_from_csv(data_file)
    log_event("Azure Entra ID simulation complete.")
