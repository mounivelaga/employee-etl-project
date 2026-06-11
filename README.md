Employee ETL Pipeline
Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, JSON, and PostgreSQL.

The pipeline extracts employee data from a JSON file, transforms and validates the data using Pandas, and loads the processed data into a PostgreSQL database.

Technologies Used
Python
Pandas
PostgreSQL
SQLAlchemy
JSON
Git & GitHub
Logging
Project Structure

employee-etl-project/

├── data/

│ └── employee_data.json

├── extract.py

├── transform.py

├── load.py

├── main.py

├── logger.py

├── config.json

├── requirements.txt

└── README.md

ETL Workflow
Extract data from JSON file.
Transform data using Pandas.
Validate required columns.
Handle missing values.
Remove duplicate records.
Load data into PostgreSQL.
Verify data using SQL queries.
Sample Input
{
  "employee_id": 101,
  "name": "John Smith",
  "department": "IT",
  "salary": 75000,
  "location": {
    "city": "Toronto"
  }
}
Transformation Steps
Flatten nested JSON using pd.json_normalize()
Validate required columns
Fill missing salary values with 0
Standardize employee names
Remove duplicate records
Database Table

Table Name: employees

Columns:

employee_id
name
department
salary
location.city
How to Run
Install Dependencies
pip install -r requirements.txt
Run the Pipeline
python main.py
Verify Data in PostgreSQL
SELECT * FROM employees;
Sample Output
employee_id	name	department	salary	location.city
101	John Smith	IT	75000	Toronto
102	Mary Johnson	Finance	68000	Brampton
103	David Lee	HR	0	Mississauga
Future Enhancements
Load data from REST APIs
Add unit testing
Implement incremental loading
Schedule pipeline execution
Add Docker support
Author

Mouni Yelisetty

Aspiring Data Engineer | Python | SQL | PostgreSQL | ETL Pipelines