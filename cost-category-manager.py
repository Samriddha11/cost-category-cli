import requests
import json
import os
import datetime

# ---------------- CONFIG ----------------
BASE_URL = "https://app.harness.io/ccm/api"
ACCOUNT_ID = "Harness-Account-ID-Here"
API_KEY = "PAT-TOKEN-HERE"
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

def backup_all_cost_categories_individual():
    print("[INFO] Backing up all cost categories...")
    mappings = list_cost_categories()
    if not mappings:
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    for cat in mappings:
        try:
            metadata = get_cost_category(cat["uuid"])
            backup_file = f"{cat['name'].replace(' ', '_')}_backup_{timestamp}.json"
            backup_path = os.path.join(BACKUP_FOLDER, backup_file)
            with open(backup_path, "w") as f:
                json.dump(metadata, f, indent=4)
            print(f"[SUCCESS] Backup created: {backup_path}")
        except Exception as e:
            print(f"[ERROR] Failed to backup {cat['name']}: {e}")

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

def restore_all_cost_categories(backup_folder=BACKUP_FOLDER, auto_rename=True):
    print(f"[INFO] Restoring all cost categories from folder: {backup_folder}")

    files = [f for f in os.listdir(backup_folder) if f.endswith(".json")]
    if not files:
        print("[INFO] No backup files found to restore.")
        return

    for file in files:
        backup_file = os.path.join(backup_folder, file)
        try:
            with open(backup_file, "r") as f:
                data = json.load(f)

            resource = data.get("resource")
            if not resource:
                print(f"[WARNING] Skipping {file} (invalid format)")
                continue

            original_name = resource.get("name", "Unnamed")
            new_name = None
            if auto_rename:
                timestamp = datetime.datetime.now().strftime("%H%M%S")
                new_name = f"{original_name}_restored_{timestamp}"

            print(f"[INFO] Restoring cost category: {original_name}")
            restore_cost_category(backup_file, new_name=new_name)

        except Exception as e:
            print(f"[ERROR] Failed to restore from {file}: {e}")

    print("[INFO] Batch restore process completed.")

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
        print("3. Backup ALL Cost Categories")
        print("4. Restore a Cost Category from Backup")
        print("5. Restore ALL Cost Categories")
        print("6. Delete a Cost Category")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            list_cost_categories()
        elif choice == "2":
            name = input("Enter the cost category name to backup: ").strip()
            backup_cost_category(name)
        elif choice == "3":
            backup_all_cost_categories_individual()
        elif choice == "4":
            backup_file = input("Enter backup file path: ").strip()
            new_name = input("Enter new name (leave blank to use original): ").strip() or None
            restore_cost_category(backup_file, new_name)
        elif choice == "5":
            restore_all_cost_categories()
        elif choice == "6":
            name = input("Enter the cost category name to delete: ").strip()
            delete_cost_category(name)
        elif choice == "7":
            print("[INFO] Exiting...")
            break
        else:
            print("[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    print("[INFO] Logged into Harness. Starting Cost Category Manager...")
    main_menu()
