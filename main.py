import json
from flask import  Flask, session, request,jsonify

from flask_sqlalchemy import SQLAlchemy
import os

from systemManager import SystemManager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=''

# @app.route('/')
# def index():
#     return 'welcome to my webpage!'

@app.route('/login', methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    result = systemManager.userLogin(username=username, password=password)
    print(result)
    return jsonify(msg="ok")
    
    

if __name__=="__main__":
    systemManager = SystemManager()    
    app.run(port=2020,host="127.0.0.1",debug=True)