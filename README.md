# Harness Cost Category Manager

A Python-based CLI utility to **backup, restore, list, and delete** Harness **Cost Categories** using the Harness CCM API.

---

## 🚀 Features

1. **List Cost Categories** – Displays all existing cost categories.
2. **Backup a Single Cost Category** – Creates a timestamped JSON backup.
3. **Backup ALL Cost Categories (Individual Files)** – Each category gets its own JSON file.
4. **Restore a Cost Category** – Restores from a backup file, optionally renaming it.
5. **Restore ALL Cost Categories** – Batch restores all JSON backups with optional `auto_rename` to prevent conflicts.
6. **Delete a Cost Category** – Deletes a category by name.

Backups are stored in the `backups/` folder for easy management.

---

## ⚙️ Setup

1. **Clone the Repository:**

```bash
git clone https://github.com/Samriddha11/cost-category-manager.git
cd cost-category-manager
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set Your Harness Credentials:**

- Update the `ACCOUNT_ID` and `API_KEY` in the script.  
- **Generate a Harness PAT Token:** [How to generate a PAT token](https://developer.harness.io/docs/platform/Automation/api/add-and-manage-api-keys)

```python
ACCOUNT_ID = "your_harness_account_id"
API_KEY = "your_pat_api_key"
```

4. **Run the Script:**

```bash
python cost_category_manager.py
```

---

## 📋 Menu Options

```
1. List Cost Categories
2. Backup a Cost Category
3. Backup ALL Cost Categories
4. Restore a Cost Category from Backup
5. Restore ALL Cost Categories
6. Delete a Cost Category
7. Exit
```

---

## 💾 Backup Examples

### Backup a Single Cost Category

```bash
Enter the cost category name to backup: Cloud_Projects
# Output:
# [INFO] Starting backup for cost category: Cloud_Projects
# [SUCCESS] Backup saved to: backups/Cloud_Projects_backup_20250729_153045.json
```

### Backup ALL Cost Categories

```bash
Select option 3 in the menu.
# Output:
# [INFO] Backing up all cost categories...
# [SUCCESS] Backup created: backups/Finance_backup_20250729_153045.json
# [SUCCESS] Backup created: backups/Engineering_backup_20250729_153045.json
```

---

## ♻️ Restore Examples

### Restore a Single Cost Category

```bash
Enter backup file path: backups/Cloud_Projects_backup_20250729_153045.json
Enter new name (leave blank to use original): Cloud_Projects_Restored
# Output:
# [INFO] Creating cost category 'Cloud_Projects_Restored'...
# [SUCCESS] Cost category 'Cloud_Projects_Restored' restored successfully!
```

### Restore ALL with Auto Rename (Default)

```bash
Select option 5 in the menu.
# Output:
# [INFO] Restoring all cost categories from folder: backups
# [INFO] Restoring cost category: Cloud_Projects
# [INFO] Creating cost category 'Cloud_Projects_restored_154512'...
# [SUCCESS] Cost category 'Cloud_Projects_restored_154512' restored successfully!
```

`auto_rename=True` ensures restored categories **won’t conflict** with existing names.

---

## 🗑 Delete Example

```bash
Enter the cost category name to delete: Old_Project
# Output:
# [INFO] Attempting to delete cost category: Old_Project
# [SUCCESS] Deleted cost category 'Old_Project'.
```

---

## 📝 Notes

- Backups are timestamped for uniqueness.
- Restoring with `auto_rename=True` prevents name conflicts.
- Ensure your PAT token has **CCM Read/Write permissions**.
