# Harness Cost Category Manager

A **Python CLI tool** to manage [Harness CCM](https://harness.io/products/cloud-cost-management/) Cost Categories (Business Mappings).  
This tool allows you to **list, backup, restore, and delete** cost categories with a simple interactive menu.

---

## Features

- ✅ **List Cost Categories** – View all existing cost categories with names and UUIDs.  
- ✅ **Backup Cost Category** – Save a selected cost category to a timestamped JSON file.  
- ✅ **Restore Cost Category** – Restore a cost category from a JSON backup (optionally with a new name).  
- ✅ **Delete Cost Category** – Delete an existing cost category by name.  
- ✅ **Organized Backups** – Automatically stores backups in the `backups/` folder with timestamps.  
- ✅ **Interactive CLI Menu** – Easy to navigate, with status logging for every action.

---

## Prerequisites

- Python 3.7+
- `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Setup

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/harness-cost-category-manager.git
cd harness-cost-category-manager
```

2. Configure your **Harness Account ID** and **API Key** in the script:

```python
ACCOUNT_ID = "your-account-id"
API_KEY = "your-personal-access-token"
```

> ⚠️ **Tip:** Use a [Harness Personal Access Token (PAT)](https://developer.harness.io/docs/platform/automation/api/authentication/) with **CCM Business Mapping permissions**.

---

## Usage

Run the script:

```bash
python cost_category_manager.py
```

### Interactive Menu

```
===== Harness Cost Category Manager =====
1. List Cost Categories
2. Backup a Cost Category
3. Restore a Cost Category from Backup
4. Delete a Cost Category
5. Exit
```

---

## Methods and Functionality

### 1. `list_cost_categories()`

Fetches and displays all cost categories for the given account:

- Shows **Name** and **UUID**
- Returns a list of cost category objects

---

### 2. `backup_cost_category(name: str)`

Creates a timestamped backup of a cost category:

- Fetches the **full JSON** of the cost category
- Stores backup in `backups/<Name>_backup_<timestamp>.json`

---

### 3. `restore_cost_category(backup_file: str, new_name: str = None)`

Restores a cost category from a JSON backup:

- **Optionally rename** the cost category on restore
- Cleans metadata (`uuid`, `createdAt`, `lastUpdatedAt`, etc.) automatically
- Posts the new category to Harness

---

### 4. `delete_cost_category(name: str)`

Deletes an existing cost category by name:

- Confirms name and finds UUID
- Issues `DELETE` request to Harness CCM API

---

## Folder Structure

```
harness-cost-category-manager/
├── cost_category_manager.py  # Main CLI script
├── backups/                  # JSON backups stored here
└── README.md                 # Project documentation
```

---

## Example Workflow

1. **List Cost Categories**  
   See all current categories and UUIDs.

2. **Backup Category**  
   ```text
   Enter the cost category name to backup: Services
   [SUCCESS] Backup saved to: backups/Services_backup_20250729_153045.json
   ```

3. **Restore from Backup**  
   ```text
   Enter backup file path: backups/Services_backup_20250729_153045.json
   Enter new name (leave blank to use original): Services Copy
   [SUCCESS] Cost category 'Services Copy' restored successfully!
   ```

4. **Delete Category**  
   ```text
   Enter the cost category name to delete: Services Copy
   [SUCCESS] Deleted cost category 'Services Copy'.
   ```

---

## Planned Enhancements

- [ ] **Backup All Categories** at once  
- [ ] **Automatic Scheduled Backup** with cron  
- [ ] **Logging to File** for audit purposes

---

## License

MIT License © 2025 [Samriddha Choudhuri]
