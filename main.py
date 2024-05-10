import json
from flask import  Flask, session, request,jsonify, make_response, Response

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# from flask_sqlalchemy import SQLAlchemy
import os, time

from systemManager import SystemManager
import requests



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
    
@app.route('/searchByText',methods=['POST'])
def searchByText():
    print(request)
    searchText = request.form['searchText']
    kNeighbor = request.form['kNeighbor']
    print("当前搜索的图像是："+searchText)
    # 调用算法模型
    url='http://127.0.0.1:5000/searchByText' #算法模型开放端口
    data = {'searchText':searchText, 'kNeighbor':kNeighbor}
    response = requests.post(url, data)
    if response.status_code == 200:
        result = json.loads(response.content)
        # print(json.loads(response.content))
        return jsonify(result)
    


@app.route('/searchByImage',methods=['POST'])
def searchByImage():
    img = request.files.get['searchImage']
    kNeighbor = request.form['kNeighbor']
    # username = session.get()
    suffix = '.' + img.filename.split('.')[-1] # 获取文件后缀名
    basedir = 'D:\\Code\\retUploadData\\'
    image_name = str(int(time.time()))+suffix
    image_path = basedir+image_name
    img.save(image_path)
    
    # 与服务器算法模型连接
    url='http://127.0.0.1:5000/searchByImage' #算法模型开放端口
    data = {'searchImage':img, 'kNeighbor':kNeighbor}
    response = requests.post(url, data=data)
    if response.status_code == 200 :
        # print(response.content)
        return jsonify(response.content)
    

@app.route('/searchBySketch',methods=['POST'])
def searchBySketch():
    return True
    
    
if __name__=="__main__":
    systemManager = SystemManager()    
    app.run(port=2020,host="127.0.0.1",debug=True)