# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Specialty as Specialty


@app.route('/specialties', methods=['GET'])
def select_specialties_data():
    c = Specialty.select_specialties()

    # If the specialties are available, show them. Otherwise error message
    if c!=None:
        return jsonify({"result":c})
    else:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/specialties/<string:id>', methods=['GET'])
def select_specialty_by_id(id):
    # text_id = request.json["text_id"]

    c = Specialty.select_where(id)

    # If the document data is available, return them
    if c!=None:
        return jsonify({"result": c})
    else:
        
        return jsonify({"result":"no data"})


# Route to insert data in specialties table
# ----------------------------------------------------------------------
@app.route('/specialties', methods=['POST'])
def insert_specialties_data():

    # Get data in json format
    specialty_id = request.json["specialty_id"]
    name = request.json["name"]
    description = request.json["description"]

    # Use the function in model
    c = Specialty.insert_spec_data(specialty_id, name, description)
    
    # If the insert was successful, return the okey msg
    if c==1:
        return jsonify({"result":"insert okey"})
    else:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/specialties
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
@app.route('/specialties/<string:specialty_id>', methods=['PUT'])
def update_specialties_data(specialty_id):

    # Get data in json format
    # text_id = request.json["text_id"]
    name = request.json["name"]
    description = request.json["description"]

    # Use the function in model
    c = Specialty.update_spec_data(specialty_id,name, description)
    
    # If the update was successful, return the okey msg
    if c ==1:
        return jsonify({"result":"okey updating data"})
    else:
        return  jsonify({"result":"no update"})

# Tests
# URL: 127.0.0.1:5000/specialties/5
# POST

# JSON:
# {
# "name":"errfe",
# "description":"otros"}


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/specialties/<string:specialty_id>", methods=['DELETE'])
def delete_specialty_data(specialty_id):
    # text_id = request.json["text_id"]
    c = Specialty.delete_spec_data(specialty_id)
    
    # If the document was deleted, return succes message, else error message
    if c==1:
        return jsonify("okey deleted")
    else:
        return jsonify("no specialty deleted")

# Test with URL: http://127.0.0.1:5000/specialties/5