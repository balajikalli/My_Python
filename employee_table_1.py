import os
import cx_Oracle

# SQL query to be executed
sql_text = """
SELECT
    SALARY
FROM
    EMPLOYEES
"""

# Database connection parameters
db_config = {
    'user': 'HR',
    'password': '<Password>',
    'dsn': 'localhost:1521/XEPDB1',
    'config_dir': os.path.join('C:', 'Users', 'bljka', 'Oracle', 'network', 'admin')
}

# Establish connection and execute the SQL query using a context manager
try:
    with cx_Oracle.connect(**db_config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_text)
            # Fetch and print each row in the result set
            for row in cursor:
                print(row)
    print("Done!!")

except cx_Oracle.DatabaseError as e:
    # Handle database errors
    error, = e.args
    print(f"Oracle-Error-Code: {error.code}")
    print(f"Oracle-Error-Message: {error.message}")
