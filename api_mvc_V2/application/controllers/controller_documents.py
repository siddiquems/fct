# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Document as Document


@app.route('/documents', methods=['GET'])
def select_documents_data():
    c = Document.select_documents()

    return jsonify({"result":c})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/documents', methods=['POST'])
def insert_documents_data():

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
    # if c:
        # return jsonify({"result":"insert okey"})
    # else:
        # 
        # return jsonify({"result":"error inserting data"})
    return jsonify({"result":"okey inserting data"})


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/documents/:id", methods=['DELETE'])
def delete_document_data():
    text_id = request.json["text_id"]
    c = Document.delete_doc_data(text_id)
    return jsonify("okey deleted")