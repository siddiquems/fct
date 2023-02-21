########################################################################
##################### CRUD APP WITH MYSQL DATABASE #####################
########################################################################

########################################################################
# Author : Siddique
# Date : 16/02/2023
########################################################################

# Import Flask modules
from flask import Flask,jsonify,request

# import MySQLdb
import controller

# app Flask, initialize
app = Flask(__name__)

try:
    # Route to insert data in documents table
    # ----------------------------------------------------------------------
    @app.route('/insert_documents_data', methods=['POST'])
    def insert_documents_data():

        # Get data in json format
        text_id = request.json["text_id"]
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in controller
        c = controller.insert_doc_data(text_id, date, author, source, collection, language)
        
        # If the insert was successful, return the okey msg
        if c:
            return jsonify({"result":"insert okey"})
        else:
            return jsonify({"result":"error inserting data"})


    # Route to insert data in corpus table
    # ----------------------------------------------------------------------
    @app.route('/insert_corpus_data', methods=['POST'])
    def insert_corpus_data():

        # Get data in json format
        corpus_id = request.json["corpus_id"]
        corpus_name = request.json["corpus_name"]
        labels = request.json["labels"]
        description = request.json["description"]
        version = request.json["version"]
        n_docs = request.json["n_docs"]

        # Use the function in controller
        c = controller.insert_cor_data(corpus_id, corpus_name, labels, description, version, n_docs)
        
        # If the insert was successful, return the okey msg
        if c:
            return jsonify({"result":"insert okey"})
        else:
            return jsonify({"result":"error inserting data"})


# To check insert_documents_data
# {
#   "text_id":"2",
#   "date":"02",
#   "author":"bsc",
#   "source":"web",
#   "collection":"col2",
#   "language":"es"
# }

except:
    msg = 'Error'
    print(msg)


# Main function
# ----------------------------------------------------------------------
if __name__=="__main__":                      
    app.run()    