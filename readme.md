# Disk Usage Analyzer

A Python-based system that analyzes disk usage by scanning folders or entire drives and storing file metadata in a MySQL database.
It provides insights such as largest files, file type distribution, search functionality, and visualization using pie charts.

---

##  Features

* Scan any folder or entire disk
* Store file metadata in MySQL database
* Identify largest files
* File type distribution analysis
* Search files by name
* Calculate total disk usage
* Pie chart visualization of file types
* Prevent duplicate entries using unique constraints
* Option to clear database manually

---

## Tech Stack

* **Python**

  * `os` → file system traversal
  * `datetime` → file timestamps
* **MySQL**

  * data storage and querying
* **Matplotlib**

  * data visualization (pie chart)
* **mysql-connector-python**

  * database connectivity

---

##  How It Works

1. The system scans a user-specified folder using `os.walk()`.
2. For each file, it extracts:

   * File name
   * Size
   * Type (extension)
   * Last modified time
   * File path
3. This data is stored in a MySQL table.
4. SQL queries are used to analyze:

   * Largest files
   * File type distribution
   * Search results
   * Total storage usage
5. Visualization is generated using Matplotlib.

---

## 📂 Project Structure

```
Disk_usage_Analyser/
│
├── main.py                  # Main menu-driven program
├── readme.md               # Project documentation
├── .gitignore              # Ignored files
│
├── database/
│   ├── config.py           # MySQL connection setup
│   └── operations.py       # Database operations (queries)
│
├── scan/
│   └── scanner.py          # File scanning logic using os module
│
├── convert/
│   ├── chart.py            # Visualization (pie chart)
│   └── cnvrt.py            # Size conversion (bytes → KB/MB/GB)
│
└── __pycache__/            # Python cache files (ignored)
```


## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/disk-usage-analyzer.git
cd disk-usage-analyzer
```

---

### 2. Install dependencies

```
pip install mysql-connector-python matplotlib
```

---

### 3. Setup MySQL database

Run the following SQL commands:

```
CREATE DATABASE IF NOT EXISTS file_analyzer;
USE file_analyzer;

CREATE TABLE IF NOT EXISTS files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    size BIGINT NOT NULL,
    type VARCHAR(50),
    modified_time DATETIME,
    path TEXT NOT NULL,
    UNIQUE KEY unique_path (path(255))
);
```

---

### 4. Configure database connection

Edit:

```
database/config.py
```

Set your credentials:

```
host = "127.0.0.1"
user = "root"
password = "your_password"
database = "file_analyzer"
```

---

### 5. Run the project

```
python main.py
```

---

## 📊 Sample Output

```
--- Disk Analyzer ---
1. Scan Folder
2. Show Largest Files
3. Show File Types
4. Search File
5. Total Size
6. Show Pie Chart
7. Clear Database
8. Exit
```

---

## 🧪 Example Use Cases

* Identify large files consuming storage
* Analyze file types in a directory
* Quickly locate specific files
* Monitor disk usage patterns

---

## ⚠️ Limitations

* Full disk scan may take time
* Requires MySQL to be running
* Permission-restricted files may be skipped

---

## 🔮 Future Improvements

* GUI interface (Tkinter / Web app)
* File deletion option for large files
* Real-time monitoring
* Bar chart visualization
* Export results to CSV

---

## 👨‍💻 Author

**Raj Patil**

---

## 📌 Notes

* Duplicate files are prevented using a unique constraint on file paths.
* Small file types can be grouped for better visualization in pie charts.

---
