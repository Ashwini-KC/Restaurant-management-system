## Restaurant Management System

## Requirements

Ensure the following dependencies are installed before running the project:

1. Python3
2. pipenv (Python virtual environment manager)
3. MySQL Server running on port 3306

## Project Initialization

Follow these steps to set up and run the project:

1. Navigate to the project directory.

    ```bash
    cd path/to/project-directory
    ```

2. Install depedecies.

    ```bash
    pipenv install
    ```
3. Configure database settings in the `properties.py` file as per your MySQL setup.
4. Open MySQL in the command line and execute the following commands to set up the database

    ```bash
    source sql/create_tables.sql;
    source sql/insert-menu.sql;
    ```
5. Run the application:

   ```bash
   pipenv run rms
   ```

## Database Schema

The system uses the following tables in MySQL:

1. Employee Table

    ```
    +---------+--------------+------+-----+---------+-------+
    | Field   | Type         | Null | Key | Default | Extra |
    +---------+--------------+------+-----+---------+-------+
    | EmpID   | varchar(255) | NO   | PRI | NULL    |       |
    | EmpName | varchar(255) | NO   |     | NULL    |       |
    | EmpType | varchar(255) | YES  |     | NULL    |       |
    +---------+--------------+------+-----+---------+-------+
    ```

2. Menu Table

    ```
    +-----------+--------------+------+-----+---------+-------+
    | Field     | Type         | Null | Key | Default | Extra |
    +-----------+--------------+------+-----+---------+-------+
    | itemID    | varchar(255) | NO   | PRI | NULL    |       |
    | itemName  | varchar(255) | NO   |     | NULL    |       |
    | itemPrice | int          | NO   |     | NULL    |       |
    | itemType  | varchar(255) | NO   |     | NULL    |       |
    +-----------+--------------+------+-----+---------+-------+
   ```

## Installing Additional Packages
Make sure to install the required packages:
```bash
pip install random_id
pip install pytest
pip install pytest-cov
```
   
### Todo

- [ ] Create tables for each class.
- [ ] Write functions for each class.
- [ ] Write test cases.
