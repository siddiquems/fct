from flask import Flask
from application import app

# Configparser settings
# --------------------------------------------------
import configparser


parameters = config = configparser.ConfigParser()
parameters.read('./configuration.cfg')


# Main function
# ----------------------------------------------------------------------
if __name__=="__main__":                      
    app.run() 


# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8000, debug=True)