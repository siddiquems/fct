# Import Flask modules
from application import app
from flask import Flask,jsonify,request


@app.route('/login', methods=['POST']) 
def login():
    
    data = request.get_json()
    username = request.json['username']
    password = request.json['password']

    # Chequea si el usuario y la contraseña son correctos 
    if username == 'admin' and password == '123':
        return jsonify({"message": "Login exitoso"})
    else:
        return jsonify({"message": "Usuario o contraseña incorrectos"})