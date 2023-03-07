# Import Flask modules
from application import app
from flask import Flask,jsonify,request
from application.models import Normalization

# Import documents model
import application.models.Document as Document


@app.route('/normalizations', methods=['GET'])
def select_normalizations_data():
    c = Normalization.select_normalizations()

    # If the normalizations are available, show them. Otherwise error message
    if c!=None:
        return jsonify({"result":c})
    else:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/normalizations/<string:id>', methods=['GET'])
def select_normalization_by_id(id):
    # text_id = request.json["text_id"]

    c = Normalization.select_where(id)

    # If the normalization data is available, return them
    if c!=None:
        return jsonify({"result": c})
    else:
        
        return jsonify({"result":"no data"})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/normalizations', methods=['POST'])
def insert_normalizations_data():

    # Get data in json format
    norm_id = request.json["norm_id"]
    ontology_id = request.json["ontology_id"]
    code_id = request.json["code_id"]
    semantic_relation = request.json["semantic_relation"]

    # Use the function in model
    c = Normalization.insert_norm_data(norm_id, ontology_id, code_id, semantic_relation)
    
    # If the insert was successful, return the okey msg
    # if c==1:
    #     return jsonify({"result":"insert okey"})
    # else:
        
    #     return jsonify({"result":"error inserting data"})
    return jsonify({"result":"okey"})

# Tests
# URL: http://127.0.0.1:5000/normalizations
# Method: POST

# JSON:
# {
#   "norm_id":6,
#   "ontology_id":"6",
#   "code_id":"23424",
#   "semantic_relation":"ceevklen"
# }


# Route to insert data in normalizations table 
# ----------------------------------------------------------------------
@app.route('/normalizations/<string:norm_id>', methods=['PUT'])
def update_normalizations_data(norm_id):

    # Get data in json format
    ontology_id = request.json["ontology_id"]
    code_id = request.json["code_id"]
    semantic_relation = request.json["semantic_relation"]

    # Use the function in model
    c = Normalization.update_norm_data(norm_id, ontology_id, code_id, semantic_relation)
    
    # If the insert was successful, return the okey msg
    if c ==1:
        return jsonify({"result":"okey updating data"})
    else:
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
@app.route("/normalizations/<string:norm_id>", methods=['DELETE'])
def delete_normalization_data(norm_id):
    # text_id = request.json["text_id"]
    c = Normalization.delete_norm_data(norm_id)
    
    # If the normalization was deleted, return succes message, else error message
    if c==1:
        return jsonify("okey deleted")
    else:
        return jsonify("no normalization deleted")

# Test with URL: http://127.0.0.1:5000/normalization/5