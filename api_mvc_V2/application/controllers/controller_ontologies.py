# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Ontology as Ontology


@app.route('/ontologies', methods=['GET'])
def select_ontologies_data():
    c = Ontology.select_ontologies()

    # If the documents are available, show them. Otherwise error message
    if c!=None:
        return jsonify({"result":c})
    else:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/ontologies/<string:ontology_id>', methods=['GET'])
def select_ontology_by_id(ontology_id):
    # text_id = request.json["text_id"]

    c = Ontology.select_where(ontology_id)

    # If the document data is available, return them
    if c!=None:
        return jsonify({"result": c})
    else:
        
        return jsonify({"result":"no data"})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/ontologies', methods=['POST'])
def insert_ontologies_data():

    # Get data in json format
    ontology_id = request.json["ontology_id"]
    name = request.json["name"]
    version = request.json["version"]
    language = request.json["language"]
    description = request.json["description"]

    # Use the function in model
    c = Ontology.insert_ont_data(ontology_id, name, version, language, description)
    
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
@app.route('/ontologies/<string:ontology_id>', methods=['PUT'])
def update_ontologies_data(ontology_id):

    # Get data in json format
    # text_id = request.json["text_id"]
    name = request.json["name"]
    version = request.json["version"]
    language = request.json["language"]
    description = request.json["description"]

    # Use the function in model
    c = Ontology.update_ont_data(ontology_id, name, version, language, description)
    
    # If the insert was successful, return the okey msg
    if c ==1:
        return jsonify({"result":"okey updating data"})
    else:
        return  jsonify({"result":"no update"})

# Tests
# URL: http://127.0.0.1:5000/ontologies/1

# JSON:
# {
# "name":"rteg",
# "version":"24",
# "language":"es",
# "description":"3u34"}


# Delete a ontology by id
# --------------------------------------------------------------------
@app.route("/ontologies/<string:ontology_id>", methods=['DELETE'])
def delete_ontology_data(ontology_id):
    # text_id = request.json["text_id"]
    c = Ontology.delete_ont_data(ontology_id)
    
    # If the ontology was deleted, return succes message, else error message
    if c==1:
        return jsonify("okey deleted")
    else:
        return jsonify("no ontology deleted")

# Test with URL: http://127.0.0.1:5000/ontologies/5