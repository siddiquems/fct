# Import Flask modules
from application import app
from flask import Flask,jsonify,request

import application.models.Corpus as Corpus



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
    # if c:
    #     return jsonify({"result":"insert okey"})
    # else:
    #     return jsonify({"result":"error inserting data"})
    return jsonify({"result":"okey inserting data"})


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/corpus", methods=["DELETE"])
def delete_corpus_data():
    corpus_id = request.json["corpus_id"]
    c = Corpus.delete_cor_data(corpus_id)
    return jsonify("okey deleted")