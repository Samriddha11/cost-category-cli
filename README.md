# Harness Cost Category Manager

A Python-based CLI tool to **list, backup, restore, and delete** [Harness](https://harness.io) CCM (Cloud Cost Management) **Cost Categories**.

This tool is useful for **backing up all cost categories individually** into JSON files for easy restore, migrating cost categories across environments, or creating automated disaster recovery workflows.

---

## **Features**

1. **List Cost Categories**  
   View all existing cost categories in your Harness account.

2. **Backup a Single Cost Category**  
   Saves a specific cost category to a JSON file with timestamp.

3. **Backup ALL Cost Categories (Individual Files)**  
   Creates separate backup JSON files for each cost category.  
   ✅ Easy restore – Each backup file contains full cost category metadata.

4. **Restore a Single Cost Category**  
   Recreates a cost category from a backup JSON file.  
   - Optionally, you can assign a new name while restoring.

5. **Restore ALL Cost Categories**  
   Restores all cost categories from the `backups/` folder.  
   - Auto-renames categories to prevent name conflicts.

6. **Delete a Cost Category**  
   Permanently deletes a cost category from Harness.

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/Samriddha11/cost-category-manager.git
cd cost-category-manager
```

2. Install dependencies (Python 3.8+ required):

```bash
pip install -r requirements.txt
```

---

## **Configuration**

Edit the following variables in the Python script:

```python
BASE_URL = "https://app.harness.io/ccm/api"
ACCOUNT_ID = "<YOUR_ACCOUNT_ID>"
API_KEY = "<YOUR_PAT_API_KEY>"
BACKUP_FOLDER = "backups"
```

- `ACCOUNT_ID` → Your Harness account identifier.
- `API_KEY` → Your Harness **Personal Access Token (PAT)**.

🔹 **How to generate a PAT token:**  
[Harness Documentation – Generating a PAT](https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/#generate-a-personal-access-token)

---

## **Usage**

Run the CLI tool:

```bash
python cost_category_manager.py
```

Menu options:

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

## **Backup Files**

- All backups are stored in the `backups/` folder.
- Each backup JSON file is named like:

```
<CostCategoryName>_backup_YYYYMMDD_HHMMSS.json
```

Example:

```
Engineering_backup_20250729_121530.json
```

---

## **Example Commands**

### **Backup a Specific Cost Category**
```bash
python cost_category_manager.py
# Choose Option 2
# Enter cost category name: Engineering
```

### **Backup All Cost Categories**
```bash
python cost_category_manager.py
# Choose Option 3
```

### **Restore All Cost Categories**
```bash
python cost_category_manager.py
# Choose Option 5
```

---

## **Notes**

- When restoring **all** cost categories, auto-renaming with a timestamp is applied to avoid conflicts.
- Only cost category configuration is backed up; cost data is not included.

---

## **License**

MIT License

---

### **Author**
**Samriddha Choudhuri**  
GitHub: [Samriddha11](https://github.com/Samriddha11)
