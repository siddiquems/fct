# ------------------------ Specialty Model -----------------------------
# Manages all the petitions from the server

# Imports
from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all documents from the database
# --------------------------------------------------------------------------------
def select_specialties():
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from specialties")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a document by id
# --------------------------------------------------------------------------------
def select_where(specialty_id):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM specialties WHERE text_id = %s", specialty_id)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_spec_data(specid, name, description):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO specialties(specialty_id, name, description) VALUES (%s, %s, %s)",
                    (specid, name, description))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


def update_spec_data(specialty_id, name, description):
    '''Input parameters: data to update in the table'''
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE specialties SET name=%s, description=%s WHERE specialty_id=%s",
                    (name, description, specialty_id))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")


# To delete data in documents table
# ---------------------------------------------------------------------------------
def delete_spec_data(specialtyid):
    '''Input parameter: the id of the specialty to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM specialties WHERE specialty_id = %s", specialtyid)

    # commit and close
    connexion.commit()
    connexion.close


# To select specilties data by text id
# ---------------------------------------------------------------------------------
def select_specialties_by_document(textid):
    '''
    Input parameters: text id to search the specialties of a specific document
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from specialties JOIN document_specialities ON specialties.specialty_id =  document_specialities.specialty_id WHERE document_specialities.text_id=%s", textid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data