#----------------------------------------------------------------------------#
# File: Corpus Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 07/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all corpus from the database
# --------------------------------------------------------------------------------
def select_corpus():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from corpus")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a corpus by id
# --------------------------------------------------------------------------------
def select_where(corpusid):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM corpus WHERE corpus_id = %s", corpusid)

    # commit and close the connection
        data = cursor.fetchall()
        return data



# Function to insert data in corpus table
# ---------------------------------------------------------------------------------
def insert_cor_data(corpus_id, corpus_name, labels, description, version, n_docs):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("INSERT INTO corpus(corpus_id, corpus_name, labels, description, version, n_docs) VALUES (%s, %s, %s, %s, %s, %s)",
                    (corpus_id, corpus_name, labels, description, version, n_docs))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


# Function to insert data in corpus table
# ---------------------------------------------------------------------------------
def update_cor_data(corpus_id, corpus_name, labels, description, version, n_docs):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("UPDATE corpus SET corpus_name = %s, labels = %s, description = %s, version = %s, n_docs = %s WHERE corpus_id = %s",
                    (corpus_name, labels, description, version, n_docs, corpus_id))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")


# To delete data in corpus table
# ---------------------------------------------------------------------------------
def delete_cor_data(corpusid):
    '''Input parameter: the id of the corpus to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM corpus WHERE corpus_id = %s", corpusid)

    # commit and close
    connexion.commit()
    connexion.close

    
# To select corpus data by text id
# ---------------------------------------------------------------------------------
def select_corpus_by_document(textid):
    '''
    Input parameters: text id to search the corpus of a specific document
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from corpus JOIN document_corpus ON corpus.corpus_id =  document_corpus.corpus_id WHERE document_corpus.text_id=%s", textid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data