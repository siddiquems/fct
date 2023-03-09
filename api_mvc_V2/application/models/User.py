# ------------------------ User Model -----------------------------
# Manages all the petitions from the server

# Imports
from pathlib import Path
from application.config.database import get_connection # Import the database connection


def get_user(username, password):

    # get connection
    conexion = get_connection()
    
    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute ('SELECT * FROM users WHERE username=%s AND password=%s',username, password)        
        
        #fetch data and return
        data = cursor.fetchone()
        return data