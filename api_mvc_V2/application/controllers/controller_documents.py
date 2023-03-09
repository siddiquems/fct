# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Document as Document

# Route to select all documents
# -------------------------------------------------------------
@app.route('/documents', methods=['GET'])
def select_documents_data():

    try:
        c = Document.select_documents()
        # print("ok")
        return jsonify({"result":c})
    except:
        return jsonify({"result":"no data available"})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['GET'])
def select_document_by_id(id):
    # text_id = request.json["text_id"]
    try:
        c = Document.select_where(id)
    # If the document data is available, return them
        return jsonify({"result": c})
    
    except:
        return jsonify({"result":"no data"})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/documents', methods=['POST'])
def insert_documents_data():

    # try:
    # Get data in json format
    text_id = request.json["text_id"]
    date = request.json["date"]
    author = request.json["author"]
    source = request.json["source"]
    collection = request.json["collection"]
    language = request.json["language"]

    # Use the function in model
    c = Document.insert_doc_data(text_id, date, author, source, collection, language)
    
    # If the insert was successful, return the okey msg
    if c==1:
        return jsonify({"result":"insert okey"})
    else:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/documents
# Method: POST

# JSON:
# {
#   "text_id":5,
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }


# Route to insert data in documents table  - No funcionality
# ----------------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['PUT'])
def update_documents_data(id):
    try:
        # Get data in json format
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in model
        c = Document.update_doc_data(id, date, author, source, collection, language)
    
    # If the insert was successful, return the okey msg
    # if c ==1:
        return jsonify({"result":"okey updating data","response":c})
    except:
        return  jsonify({"result":"no update"})

# Tests
# URL: http://127.0.0.1:5000/documents/1

# JSON:
# {
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/documents/<string:id>", methods=['DELETE'])
def delete_document_data(id):

    # If the document was deleted, return succes message, else error message
    try:
        c = Document.delete_doc_data(id)
        return jsonify("okey deleted")
    except:
        return jsonify("no document deleted")

# Test with URL: http://127.0.0.1:5000/documents/5