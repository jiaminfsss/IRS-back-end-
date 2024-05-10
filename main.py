import json
from flask import  Flask, session, request,jsonify, make_response, Response

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# from flask_sqlalchemy import SQLAlchemy
import os

from systemManager import SystemManager



app=Flask(__name__)
app.secret_key='retrievalSystem'

# token信息相关
app.config['JWT_SECRET_KEY']='retrievalSystem'
jwt = JWTManager(app)
# app.config['SQLALCHEMY_DATABASE_URI']=''

@app.route('/login', methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    result = systemManager.userLogin(username=username, password=password)
    response=Response()
    
    if result[0] == 1:
        result = result[1]
        
        # session
        session['username'] = username
        session['uid'] = result['uid']
        session['urole']=result['urole']
        
        # cookie与response
        response.data='登陆成功'
        response.set_cookie('username',result['uname'])
        response.set_cookie('uid',str(result['uid']))
        response.set_cookie('urole',result['urole'])
    else:
        response.data='用户名或密码错误'
    return response
    
@app.route('/groupSearchByUserID', methods=['GET'])
def groupSearchByUserID():
    username=session.get('username')
    return username
    

if __name__=="__main__":
    systemManager = SystemManager()    
    app.run(port=2020,host="127.0.0.1",debug=True)