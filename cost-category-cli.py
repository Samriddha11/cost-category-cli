import requests
import json
import os
import datetime

# ---------------- CONFIG ----------------
BASE_URL = "https://app.harness.io/ccm/api"
ACCOUNT_ID = "Harness-Account-ID-Here"
API_KEY = "APIKEYHERE"
BACKUP_FOLDER = "backups"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

os.makedirs(BACKUP_FOLDER, exist_ok=True)

# ---------------- FUNCTIONS ----------------
def list_cost_categories():
    url = f"{BASE_URL}/business-mapping?accountIdentifier={ACCOUNT_ID}"
    print("[INFO] Fetching cost categories...")
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"[ERROR] Failed to fetch categories: {resp.text}")
        return []
    data = resp.json().get("resource", {}).get("businessMappings", [])
    if not data:
        print("[INFO] No cost categories found.")
    else:
        print("\n[INFO] Existing Cost Categories:")
        for idx, cat in enumerate(data, 1):
            print(f"  {idx}. {cat['name']} (UUID: {cat['uuid']})")
    return data

def get_cost_category(uuid):
    url = f"{BASE_URL}/business-mapping/{uuid}?accountIdentifier={ACCOUNT_ID}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def backup_cost_category(name):
    print(f"[INFO] Starting backup for cost category: {name}")
    mappings = list_cost_categories()
    target = next((m for m in mappings if m["name"] == name), None)
    if not target:
        print(f"[ERROR] Cost category '{name}' not found.")
        return
    metadata = get_cost_category(target["uuid"])
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_FOLDER, f"{name.replace(' ', '_')}_backup_{timestamp}.json")
    with open(backup_path, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"[SUCCESS] Backup saved to: {backup_path}")

def restore_cost_category(backup_file, new_name=None):
    print(f"[INFO] Restoring cost category from backup: {backup_file}")
    with open(backup_file, "r") as f:
        data = json.load(f)

    resource = data.get("resource")
    if not resource:
        print("[ERROR] Invalid backup file.")
        return

    # Clean and prepare data
    resource.pop("uuid", None)
    resource["name"] = new_name if new_name else resource["name"]
    for field in ["createdAt", "lastUpdatedAt", "createdBy", "lastUpdatedBy"]:
        resource.pop(field, None)

    url = f"{BASE_URL}/business-mapping?accountIdentifier={ACCOUNT_ID}"
    print(f"[INFO] Creating cost category '{resource['name']}'...")
    resp = requests.post(url, headers=HEADERS, json=resource)
    if resp.status_code == 200:
        print(f"[SUCCESS] Cost category '{resource['name']}' restored successfully!")
    else:
        print(f"[ERROR] Restore failed: {resp.text}")

def delete_cost_category(name):
    print(f"[INFO] Attempting to delete cost category: {name}")
    mappings = list_cost_categories()
    target = next((m for m in mappings if m["name"] == name), None)
    if not target:
        print(f"[ERROR] Cost category '{name}' not found.")
        return
    url = f"{BASE_URL}/business-mapping/{target['uuid']}?accountIdentifier={ACCOUNT_ID}"
    resp = requests.delete(url, headers=HEADERS)
    if resp.status_code == 200:
        print(f"[SUCCESS] Deleted cost category '{name}'.")
    else:
        print(f"[ERROR] Deletion failed: {resp.text}")

# ---------------- MENU INTERFACE ----------------
def main_menu():
    while True:
        print("\n===== Harness Cost Category Manager =====")
        print("1. List Cost Categories")
        print("2. Backup a Cost Category")
        print("3. Restore a Cost Category from Backup")
        print("4. Delete a Cost Category")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            list_cost_categories()
        elif choice == "2":
            name = input("Enter the cost category name to backup: ").strip()
            backup_cost_category(name)
        elif choice == "3":
            backup_file = input("Enter backup file path: ").strip()
            new_name = input("Enter new name (leave blank to use original): ").strip() or None
            restore_cost_category(backup_file, new_name)
        elif choice == "4":
            name = input("Enter the cost category name to delete: ").strip()
            delete_cost_category(name)
        elif choice == "5":
            print("[INFO] Exiting...")
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    print("[INFO] Logged into Harness. Starting Cost Category Manager...")
    main_menu()
