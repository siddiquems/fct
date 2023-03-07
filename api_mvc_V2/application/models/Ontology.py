# ------------------------ Ontologies Model -----------------------------
# Manages all the petitions from the server

# Imports
from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all documents from the database
# --------------------------------------------------------------------------------
def select_ontologies():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from ontologies")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a ontology by id
# --------------------------------------------------------------------------------
def select_where(ontology_id):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM ontologies WHERE ontology_id = %s", ontology_id)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in ontologies table
# ---------------------------------------------------------------------------------
def insert_ont_data(ontology_id, name, version, language, description):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO ontologies(ontology_id, name, version, language, description) VALUES (%s, %s, %s, %s, %s)",
                    (ontology_id, name, version, language, description))

    # commit and close the connection
    conexion.commit()
    conexion.close()


def update_ont_data(ontology_id, name, version, language, description):

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE ontologies SET name=%s, version=%s, language=%s, description=%s WHERE ontology_id=%s",
                    (name, version, language, description, ontology_id))

    # commit and close the connection
    conexion.commit()
    print(cursor.rowcount, "record(s) updated")
    return cursor.rowcount
    # conexion.close()


# To delete data in documents table
# ---------------------------------------------------------------------------------
def delete_ont_data(ontology_id):
    '''Input parameter: the id of the ontology to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM ontologies WHERE ontology_id = %s", ontology_id)

    # commit and close
    connexion.commit()
    connexion.close