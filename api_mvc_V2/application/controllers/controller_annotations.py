# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
import application.models.Annotation as Annotation


@app.route('/annotations', methods=['GET'])
def select_annotations_data():
    c = Annotation.select_annotations()

    # If the annotations are available, show them. Otherwise error message
    if c!=None:
        return jsonify({"result":c})
    else:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})



# Route to insert data in annotations table
# ----------------------------------------------------------------------
@app.route('/annotations', methods=['POST'])
def insert_annotations_data():

    # Get data in json format
    ann_id = request.json["ann_id"]
    corpus_is = request.json["corpus_is"]
    text_id = request.json["text_id"]
    ann_text = request.json["ann_text"]
    start_span = request.json["start_span"]
    end_span = request.json["end_span"]
    norm_id = request.json["norm_id"]
    attributes = request.json["attributes"]
    mark = request.json["mark"]

    # Use the function in model
    c = Annotation.insert_ann_data(ann_id, corpus_is, text_id, ann_text, start_span, end_span, norm_id, attributes, mark)
    
    # If the insert was successful, return the okey msg
    if c==1:
        return jsonify({"result":"insert okey"})
    else:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/annotations
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


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/annotations/<string:id>', methods=['PUT'])
def update_annotations_data(id):

    # Get data in json format
    # text_id = request.json["text_id"]
    ann_id = request.json["ann_id"]
    corpus_is = request.json["corpus_is"]
    text_id = request.json["text_id"]
    ann_text = request.json["ann_text"]
    start_span = request.json["start_span"]
    end_span = request.json["end_span"]
    norm_id = request.json["norm_id"]
    attributes = request.json["attributes"]
    mark = request.json["mark"]

    # Use the function in model
    c = Annotation.update_ann_data(ann_id, corpus_is, text_id, ann_text, start_span, end_span, norm_id, attributes, mark)
    
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
@app.route("/annotations/<string:id>", methods=['DELETE'])
def delete_annotation_data(id):
    # text_id = request.json["text_id"]
    c = Annotation.delete_ann_data(id)
    
    # If the document was deleted, return succes message, else error message
    if c==1:
        return jsonify("okey deleted")
    else:
        return jsonify("no annotation deleted")

# Test with URL: http://127.0.0.1:5000/documents/5