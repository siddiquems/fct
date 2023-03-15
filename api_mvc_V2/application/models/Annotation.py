#----------------------------------------------------------------------------#
# File: Annotations Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 10/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path
from application.config.database import get_connection # Import the database connection



# Function to select all annotations from the database
# --------------------------------------------------------------------------------
def select_annotations():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from annotations")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    


# Function to insert data in annotations table
# ---------------------------------------------------------------------------------
def insert_ann_data(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("INSERT INTO annotations(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")



# Function to update data in annotations table
# ---------------------------------------------------------------------------------
def update_ann_data(ann_id, corpus_is, text_id, ann_text, start_span, end_span, norm_id, attributes, mark):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("UPDATE annotations SET corpus_id = %s, text_id = %s, ann_text = %s, start_span = %s, end_span = %s, norm_id = %s, attributes = %s, mark = %s WHERE ann_id = %s",
                    (corpus_is, text_id, ann_text, start_span, end_span, norm_id, attributes, mark, ann_id))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")


# To delete data in annotations table
# ---------------------------------------------------------------------------------
def delete_ann_data(annid):
    '''Input parameter: the id of the corpus to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM annnotations WHERE ann_id = %s", annid)

    # commit and close
    connexion.commit()
    connexion.close