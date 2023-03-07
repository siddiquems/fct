# Import Flask modules
from application import app
from flask import Flask,jsonify,request

import application.models.Corpus as Corpus

@app.route('/corpus', methods=['GET'])
def select_corpus_data():
    c = Corpus.select_corpus()

    # If the documents are available, show them. Otherwise error message
    if c!=None:
        return jsonify({"result":c})
    else:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a document by id
# -------------------------------------------------------------
@app.route('/corpus/<string:id>', methods=['GET'])
def select_corpus_by_id(id):
    # text_id = request.json["text_id"]

    c = Corpus.select_where(id)

    # If the document data is available, return them
    if c!=None:
        return jsonify({"result": c})
    else:
        
        return jsonify({"result":"no data"})



# Route to insert data in corpus table
# ----------------------------------------------------------------------
@app.route('/corpus', methods=['POST'])
def insert_corpus_data():

    # Get data in json format
    corpus_id = request.json["corpus_id"]
    corpus_name = request.json["corpus_name"]
    labels = request.json["labels"]
    description = request.json["description"]
    version = request.json["version"]
    n_docs = request.json["n_docs"]

    # Use the function in model
    c = Corpus.insert_cor_data(corpus_id, corpus_name, labels, description, version, n_docs)
    
    # If the insert was successful, return the okey msg
    if c==1:
        return jsonify({"result":"insert okey"})
    else:
        
        return jsonify({"result":"error inserting data"})


# To test
# URL: http://127.0.0.1:5000/corpus
# Method: POST

# {
#   "corpus_id" : "12",
#   "corpus_name":"corpus_dishf",
#   "labels":"label11",
#   "description":"Corpus description",
#   "version":"2.0",
#   "n_docs":"2"
# }


# Route to update data in corpus table - OK
# ----------------------------------------------------------------------
@app.route('/corpus/<string:corpus_id>', methods=['PUT'])
def update_corpus_data(corpus_id):

    # Get data in json format
    corpus_name = request.json["corpus_name"]
    labels = request.json["labels"]
    description = request.json["description"]
    version = request.json["version"]
    n_docs = request.json["n_docs"]

    # Use the function in model
    c = Corpus.update_cor_data(corpus_id, corpus_name, labels, description, version, n_docs)
    
    # If the insert was successful, return the okey msg
    if c ==1:
        return jsonify({"result":"okey updating data"})
    else:
        return  jsonify({"result":"no update"})

# Test
# 127.0.0.1:5000/corpus/12
# Method = PUT

# {
#   "corpus_name":"deede",
#   "labels":"label11",
#   "description":"Corpus description",
#   "version":"2.0",
#   "n_docs":"2"
# }


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/corpus/<string:corpusid>", methods=['DELETE'])
def delete_corpus_data(corpusid):

    c = Corpus.delete_cor_data(corpusid)

    # If the corpus was deleted, return succes message, else error message
    if c==1:
        return jsonify("okey deleted")
    else:
        return jsonify("no corpus deleted")