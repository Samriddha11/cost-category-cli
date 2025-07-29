# Harness Cost Category Manager

Harness Cost Category Manager is a Python-based CLI tool to manage **Cost Categories (Business Mappings)** in Harness Cloud Cost Management (CCM).  
It allows you to **list, backup, restore, and delete** cost categories easily, with both individual and bulk operations.

## Features

- ✅ List all existing cost categories
- ✅ Backup a single cost category to a JSON file
- ✅ Backup all cost categories (each as a separate JSON file for easy restore)
- ✅ Restore a single cost category from a backup file
- ✅ Restore all cost categories from a backup folder (with optional auto-renaming to avoid conflicts)
- ✅ Delete a cost category by name

## Installation

```bash
# Clone this repository
git clone https://github.com/Samriddha11/cost-category-manager.git
cd cost-category-manager

# Install dependencies
pip install -r requirements.txt
```

Requirements:
- Python 3.8+
- `requests` library

## Configuration

Update the top section of `cost_category_manager.py` with your Harness account details:

```python
BASE_URL = "https://app.harness.io/ccm/api"
ACCOUNT_ID = "YOUR_ACCOUNT_ID"
API_KEY = "YOUR_HARNESS_PAT_TOKEN"
BACKUP_FOLDER = "backups"
```

### Generating a Harness PAT Token

Follow the official Harness guide to generate a PAT token:  
🔗 [Harness: Generate a Personal Access Token](https://developer.harness.io/docs/platform/user-management/personal-access-tokens)

## Usage

Run the script to open the interactive CLI menu:

```bash
python cost_category_manager.py
```

You will see:

```
===== Harness Cost Category Manager =====
1. List Cost Categories
2. Backup a Cost Category
3. Backup ALL Cost Categories
4. Restore a Cost Category from Backup
5. Restore ALL Cost Categories
6. Delete a Cost Category
7. Exit
```

### Examples

#### 1. List all cost categories

```
Select an option: 1

[INFO] Existing Cost Categories:
  1. AWS_Prod (UUID: abc123)
  2. Azure_Dev (UUID: xyz456)
```

#### 2. Backup a single cost category

```
Select an option: 2
Enter the cost category name to backup: AWS_Prod
[INFO] Starting backup for cost category: AWS_Prod
[SUCCESS] Backup saved to: backups/AWS_Prod_backup_20250729_153045.json
```

#### 3. Backup all cost categories

```
Select an option: 3
[INFO] Backing up all cost categories...
[SUCCESS] Backup created: backups/AWS_Prod_backup_20250729_153045.json
[SUCCESS] Backup created: backups/Azure_Dev_backup_20250729_153045.json
```

#### 4. Restore a single cost category

```
Select an option: 4
Enter backup file path: backups/AWS_Prod_backup_20250729_153045.json
Enter new name (leave blank to use original): AWS_Prod_Restored
[SUCCESS] Cost category 'AWS_Prod_Restored' restored successfully!
```

#### 5. Restore all cost categories

```
Select an option: 5
[INFO] Restoring all cost categories from folder: backups
[INFO] Restoring cost category: AWS_Prod
[SUCCESS] Cost category 'AWS_Prod_restored_153045' restored successfully!
[INFO] Restoring cost category: Azure_Dev
[SUCCESS] Cost category 'Azure_Dev_restored_153046' restored successfully!
```

#### 6. Delete a cost category

```
Select an option: 6
Enter the cost category name to delete: AWS_Prod_Restored
[SUCCESS] Deleted cost category 'AWS_Prod_Restored'.
```

---

### Notes
- Backups are stored in the `backups/` folder with timestamps.
- Restoring with `auto_rename=True` prevents name conflicts.
- Make sure your PAT token has **CCM read/write** permissions.
