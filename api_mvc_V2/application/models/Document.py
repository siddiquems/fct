# ------------------------ Document Model -----------------------------
# Manages all the petitions from the server

# Imports
from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all documents from the database
# --------------------------------------------------------------------------------
def select_documents():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from documents")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a document by id
# --------------------------------------------------------------------------------
def select_where(textid):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM documents WHERE text_id = %s", textid)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_doc_data(textid, date, author, source, collection, language):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO documents(text_id, date, author, source, collection, language) VALUES (%s, %s, %s, %s, %s, %s)",
                    (textid, date, author, source, collection, language))

    # commit and close the connection
    conexion.commit()
    conexion.close()


def update_doc_data(textid, date, author, source, collection, language):

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE documents SET date=%s, author=%s, source=%s, collection=%s, language=%s WHERE text_id=%s",
                    (date, author, source, collection, language, textid))

    # commit and close the connection
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")
    # return cursor.rowcount
    # conexion.close()


# To delete data in documents table
# ---------------------------------------------------------------------------------
def delete_doc_data(textid):
    '''Input parameter: the id of the document to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM documents WHERE text_id = %s", textid)

    # commit and close
    connexion.commit()
    connexion.close