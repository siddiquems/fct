# ----------------------------- CONNECTION WITH DATABASE ----------------------------------
# This file have a function called get_connection to connect to the database


# Import
import pymysql

# Function Get connection with database
# -----------------------------------------------------------------------------------------

# class Database:
#     def get_connection():
#         return pymysql.connect( host='localhost', user= 'username', passwd='password', db='fct')

def get_connection():
        return pymysql.connect( host='localhost', user= 'username', passwd='password', db='fct')

# For testing here
# -----------------------------------------------------------------------------------------
conn = pymysql.connect( host='localhost', user= 'username', passwd='password', db='fct')

# Cursor
cursor = conn.cursor()

# Select
# print(cursor.execute('SELECT author FROM documents'))
# conn.commit()

# Insert values
# cursor.execute("INSERT INTO documents VALUES ('1', '2023-02-16', 'bsc', 'web', 'col1', 'es');")
# conn.commit()

# cursor.execute('describe documents')
# cursor.execute('INSERT INTO games VALUES(1, uno, ')

