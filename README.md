# Restaurant Management System

## Requirements

1) Python3
1) pipenv
1) MySQL server running on port 3306

## Initialise project

1) cd into the project directory and install the depedecies.

    ```bash
    pipenv install
    ```

1) In properties.py file change the configurations.

1) Run queries in in the mysql shell from files in the sql folder.

1) Implement the code in main.py and run

    ```bash
    pipenv run rms
    ```

## Tables in MYSQL

1) Table name -> employee

    ```
    +---------+--------------+------+-----+---------+-------+
    | Field   | Type         | Null | Key | Default | Extra |
    +---------+--------------+------+-----+---------+-------+
    | EmpID   | varchar(255) | NO   | PRI | NULL    |       |
    | EmpName | varchar(255) | NO   |     | NULL    |       |
    | EmpType | varchar(255) | YES  |     | NULL    |       |
    +---------+--------------+------+-----+---------+-------+
    ```

1) Table name -> menu

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

### Todo

- [ ] Create tables for each class.
- [ ] Write functions for each class.
- [ ] Write test cases.
