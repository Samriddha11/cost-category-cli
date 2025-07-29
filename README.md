# Harness Cost Category Manager

A Python utility to **manage Harness CCM Cost Categories** via the Harness API.  
It supports:

- Listing all cost categories
- Backing up a single cost category
- **Backing up all cost categories individually** (easy to restore)
- Restoring a cost category from a backup
- **Restoring all cost categories from backups**
- Deleting a cost category

---

## 🔧 Features

1. **List Cost Categories**  
2. **Backup a Single Cost Category**  
3. **Backup All Cost Categories (Individual JSON files)**  
4. **Restore a Single Cost Category**  
5. **Restore All Cost Categories from Backups**  
6. **Delete a Cost Category**  
7. **Interactive Menu Interface**  

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/Samriddha11/cost-category-manager.git
cd cost-category-manager
```

2. Install dependencies:

```bash
pip install requests
```

---

## ⚙️ Configuration

Update the **config** section at the top of `cost_category_manager.py`:

```python
BASE_URL = "https://app.harness.io/ccm/api"
ACCOUNT_ID = "your_account_id"
API_KEY = "your_personal_access_token"
BACKUP_FOLDER = "backups"
```

- `API_KEY` should be a Harness **Personal Access Token (PAT)**.
- Backups will be stored in the `backups/` folder by default.

---

## 🚀 Usage

Run the script:

```bash
python cost_category_manager.py
```

You will see the interactive menu:

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

### 1️⃣ List Cost Categories

```bash
Select an option: 1
[INFO] Existing Cost Categories:
  1. Marketing (UUID: xxxx-xxxx)
  2. Engineering (UUID: yyyy-yyyy)
```

---

### 2️⃣ Backup a Single Cost Category

Creates a timestamped JSON backup for the selected cost category:

```bash
Select an option: 2
Enter the cost category name to backup: Marketing
[SUCCESS] Backup saved to: backups/Marketing_backup_20250729_120000.json
```

---

### 3️⃣ Backup ALL Cost Categories

Creates **individual JSON files** for each cost category:

```
Select an option: 3
[SUCCESS] Backup created: backups/Marketing_backup_20250729_120000.json
[SUCCESS] Backup created: backups/Engineering_backup_20250729_120000.json
```

Result:

```
backups/
 ├─ Marketing_backup_20250729_120000.json
 ├─ Engineering_backup_20250729_120000.json
```

---

### 4️⃣ Restore a Single Cost Category

```bash
Select an option: 4
Enter backup file path: backups/Marketing_backup_20250729_120000.json
Enter new name (leave blank to use original): MarketingCopy
[SUCCESS] Cost category 'MarketingCopy' restored successfully!
```

---

### 5️⃣ Restore ALL Cost Categories

Restores **all JSON files** in the backups folder.  
By default, names are **auto-renamed** to avoid conflicts:

```
Select an option: 5
[INFO] Restoring cost category: Marketing
[SUCCESS] Cost category 'Marketing_restored_120301' restored successfully!
```

---

### 6️⃣ Delete a Cost Category

```bash
Select an option: 6
Enter the cost category name to delete: MarketingCopy
[SUCCESS] Deleted cost category 'MarketingCopy'.
```

---

## 📁 Backup & Restore Tips

- Each JSON file stores **full cost category details**.  
- **UUIDs and timestamps** are automatically removed during restore.  
- `restore_all_cost_categories()` auto-renames categories if `auto_rename=True` to prevent name collisions.

---

## 📝 License

This project is licensed under the **MIT License**.
