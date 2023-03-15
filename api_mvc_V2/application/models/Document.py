# ------------------------------ Document Model ----------------------------------
# Manages all the petitions from the server

# Imports
from pathlib import Path

# Import the database connection configuration
from application.config.database import get_connection 


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
def select_where(textid:str):
    '''
    Input parameters: 
                    textid: id of the document to find
    '''

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
def insert_doc_data(textid:str, date:str, author:str, source:str, collection:str, language:str):
    '''
    Input parameters: 
                    text id: id of the document to insert
                    date: date of the document
                    author : the author
                    source: source of the document
                    collection: collection of the document
                    langauge: in which language the document is
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO documents(text_id, date, author, source, collection, language) VALUES (%s, %s, %s, %s, %s, %s)",
                    (textid, date, author, source, collection, language))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


# Function to update data in documents table
# ---------------------------------------------------------------------------------
def update_doc_data(textid:str, date:str, author:str, source:str, collection:str, language:str):
    '''
    Input parameters: 
                    text id: id of the document to update
                    date: date of the document
                    author : the author
                    source: source of the document
                    collection: collection of the document
                    langauge: in which language the document is
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE documents SET date=%s, author=%s, source=%s, collection=%s, language=%s WHERE text_id=%s",
                    (date, author, source, collection, language, textid))

    # commit and return a message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")



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

    # commit and close connection
    connexion.commit()
    connexion.close