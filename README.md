# Harness Cost Category Manager

This Python utility allows you to **manage Harness CCM (Cloud Cost Management) cost categories** from the command line.
It supports **backup, restore, batch backup/restore, and deletion** of cost categories using the Harness API.

---

## **Features**
- ✅ List all cost categories
- ✅ Backup individual cost categories to JSON
- ✅ Backup **all** cost categories into individual JSON files
- ✅ Restore a cost category from a backup file
- ✅ Restore **all** cost categories from a backup folder
  - Supports **`auto_rename`** to avoid name conflicts during restore
- ✅ Delete cost categories
- ✅ Interactive CLI menu interface

---

## **Requirements**

- Python 3.x
- `requests` library

Install dependencies:

```bash
pip install requests
```

---

## **Setup**

1. Clone the repository:

```bash
git clone https://github.com/Samriddha11/cost-category-manager.git
cd cost-category-manager
```

2. Configure your **Harness Account** in the script:

```python
ACCOUNT_ID = "YOUR_ACCOUNT_ID"
API_KEY = "YOUR_PAT_TOKEN"
```

3. Generate a **Harness Personal Access Token (PAT)** by following the guide:  
[Harness Documentation: Generate PAT Token](https://developer.harness.io/docs/platform/user-management/personal-access-tokens/)

4. Create a folder named `backups` (the script also auto-creates it if missing).

---

## **CLI Menu**

When you run the script:

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

---

## **Examples**

### 1️⃣ Backup a single cost category

```
Enter the cost category name to backup: Production
[SUCCESS] Backup saved to: backups/Production_backup_20250729_120512.json
```

---

### 2️⃣ Backup **all** cost categories

```
[INFO] Backing up all cost categories...
[SUCCESS] Backup created: backups/Production_backup_20250729_120512.json
[SUCCESS] Backup created: backups/Development_backup_20250729_120512.json
```

---

### 3️⃣ Restore **all** cost categories with `auto_rename`

```
Select option: 5
Enable auto-rename to avoid conflicts? (y/n): y
[INFO] Restoring cost category: Production
[SUCCESS] Cost category 'Production_restored_145233' restored successfully!
```

If a category with the same name exists, auto-rename will add `_restored_<timestamp>` to the name.

---

### 4️⃣ Restore **all** cost categories without `auto_rename`

```
Select option: 5
Enable auto-rename to avoid conflicts? (y/n): n
[INFO] Restoring cost category: Production
[ERROR] Restore failed: {"status":"CONFLICT","message":"Cost category with name 'Production' already exists."}
```

---

### 5️⃣ Delete a cost category

```
Enter the cost category name to delete: Production
[SUCCESS] Deleted cost category 'Production'.
```

---

## **Batch Backup & Restore Notes**

- Backups are stored as **individual JSON files** per cost category for easy restore.
- `restore_all_cost_categories(auto_rename=True)` prevents conflicts by renaming duplicates.
- When `auto_rename=False`, restore will fail if a category with the same name exists.

---

## **Author**
**Samriddha Choudhuri**

GitHub: [Samriddha11](https://github.com/Samriddha11/cost-category-manager)
