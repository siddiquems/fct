#----------------------------------------------------------------------------#
# Ontologies Controller
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Ontology as Ontology


# Route to select all ontologies
# ----------------------------------------------------------
@app.route('/ontologies', methods=['GET'])
def select_ontologies_data():

    try:
        response = Ontology.select_ontologies()

        # If the documents are available, show them. Otherwise error message
        return jsonify({"result": "ok finding ontologies", "response":response})
    
    except:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a ontology by id
# -------------------------------------------------------------
@app.route('/ontologies/<string:ontology_id>', methods=['GET'])
def select_ontology_by_id(ontology_id):

    try:
        result = Ontology.select_where(ontology_id)

        # If the document data is available, return them
        return jsonify({"result": result})

    except:
        
        return jsonify({"result":"no data"})


# Route to insert data in ontologies table
# ----------------------------------------------------------------------
@app.route('/ontologies', methods=['POST'])
def insert_ontologies_data():

    try:
        # Get data in json format
        ontology_id = request.json["ontology_id"]
        name = request.json["name"]
        version = request.json["version"]
        language = request.json["language"]
        description = request.json["description"]

        # Use the function in model
        result = Ontology.insert_ont_data(ontology_id, name, version, language, description)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})

    except:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/ontologies
# Method: POST

# JSON:
# {
#   
# }


# Route to insert data in ontologies table 
# ----------------------------------------------------------------------
@app.route('/ontologies/<string:ontology_id>', methods=['PUT'])
def update_ontologies_data(ontology_id):

    try:
        # Get data in json format
        name = request.json["name"]
        version = request.json["version"]
        language = request.json["language"]
        description = request.json["description"]

        # Use the function in model
        response = Ontology.update_ont_data(ontology_id, name, version, language, description)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
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

    try:
        result = Ontology.delete_ont_data(ontology_id)
    
        # If the ontology was deleted, return succes message, else error message
        return jsonify("okey deleted")

    except:
        return jsonify("no ontology deleted")

# Test with URL: http://127.0.0.1:5000/ontologies/5