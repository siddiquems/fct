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
    @app.route('/insert_data', methods=['POST'])
    def insert_data():
        text_id = request.json["text_id"]
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]
        controller.insert_data(text_id, date, author, source, collection, language)
        
        return jsonify({"result":"insert okey"})

# To check
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
if __name__=="__main__":                      
    app.run()    