#----------------------------------------------------------------------------#
# File: Documents Controller
# Description: Manages all the routes and data for the Documents table
# Author : Siddique Muhammad
# Date: 13/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import Model for documents
import application.models.Document as Document


#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all documents
# -------------------------------------------------------------
@app.route('/documents', methods=['GET'])
def select_documents_data():

    # try to find all documents, except error.
    try:

        # use the function in Document model
        response = Document.select_documents()

        # return the documents as the response
        return jsonify({"result": "ok finding documents", "response":response})
    
    except:

        # error message as the result
        return jsonify({"result":"no data available"})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['GET'])
def select_document_by_id(id):
    '''
    Input parameters: id of the document to find
    '''

    # try to select a document by id except error
    try:
        document = Document.select_where(id)

        # If the document data is available, return them
        return jsonify({"result": "ok finding documents","response":document})
    
    except:
        return jsonify({"result":"no data"})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/documents', methods=['POST'])
def insert_documents_data():

    # try to insert a document data, if not possible return an error message as a result
    try:
        # Get data in json format
        text_id = request.json["text_id"]
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in model
        result = Document.insert_doc_data(text_id, date, author, source, collection, language)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:
        return jsonify({"result":"error inserting data"})

# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/documents
# Method: POST

# JSON example data:
# {
#   "text_id":5,
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }
# -----------------------------------------


# Route to update data in documents table
# ----------------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['PUT'])
def update_documents_data(id):
    '''
    Input parameters: id of the document to update
    '''

    # try to update a document's data except error
    try:

        # Get data in json format
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in model
        response = Document.update_doc_data(id, date, author, source, collection, language)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
        return  jsonify({"result":"no update"})

# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/documents/5
# Method: PUT

# JSON data:
# {
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }
# -----------------------------------------


# Route to delete data in documents table
# --------------------------------------------------------------------
@app.route("/documents/<string:id>", methods=['DELETE'])
def delete_document_data(id):
    '''
    Input parameters: id of the document to delete
    '''

    # If the document was deleted, return succes message, else error message
    try:
        # Use the function in model
        result = Document.delete_doc_data(id)
        return jsonify({"result":"okey deleted"})
    
    except:
        return jsonify({"result":"no document deleted"})

# -------- For testing this route: -------
# Test with URL: http://127.0.0.1:5000/documents/5
# Method: PUT
# -----------------------------------------


# Route to select documents in corpus
# Return documents
# -----------------------------------------------------------------------
@app.route("/documents-by-corpus/<string:corpusid>", methods=['GET'])
def select_documents_corpus(corpusid):
    '''
    Input parameters: corpus id to search the documents of a specific corpus
    '''

    # Try to find all the documents of a specific corpus, except error.
    try:

        # Use the function in Document Model
        result = Document.select_documents_by_corpus(corpusid)

        # Return success message and the data found
        return jsonify({"result": "okey finding documents", "response":result})

    except:

        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/documents-by-corpus/13
# 127.0.0.1:5000/documents-by-corpus/14
# 127.0.0.1:5000/documents-by-corpus/222

# Method GET


# Route to select documents in specialty
# Return documents
# -----------------------------------------------------------------------
@app.route("/documents-by-specialty/<string:specialityid>", methods=['GET'])
def select_documents_specility(specialityid):
    '''
    Input parameters: specility id to search the documents of a specific specility
    '''

    # Try to find all the documents of a specific specility, except error.
    try:

        # Use the function in Document Model
        result = Document.select_documents_by_specialty(specialityid)

        # Return success message and the data found
        return jsonify({"result": "okey finding documents", "response":result})

    except:
    
        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/documents-by-specility/1
# 127.0.0.1:5000/documents-by-specility/2
# 127.0.0.1:5000/documents-by-specility/3

# Method GET