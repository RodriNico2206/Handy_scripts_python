import oracledb

def execute_sql_script(sql_script, connection_info):
    # Establish connection
    connection = oracledb.connect(**connection_info)

    # Create a cursor
    cursor = connection.cursor()

    try:
        # Execute SQL script
        cursor.execute(sql_script)

        # Fetch results if any
        if cursor.description:
            result = cursor.fetchone()[0]
            return result.strftime('%d/%m/%y %H:%M:%S')

    except Exception as e:
        print("Error executing SQL script:", e)

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

# Example usage
sql_script = """
SELECT SYSDATE FROM DUAL
"""

connection_info = {
    'user': 'Gravity',
    'password': '123',
    'dsn': 'localhost:1521/xe'
}

sysdate = execute_sql_script(sql_script, connection_info)
print(sysdate)