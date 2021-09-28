# -*- coding:UTF-8 -*-
import json
import re
from flask import Flask, request
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):
        # 将获取到的json数据转为字典
        body=json.loads(request.data)
        msg = body['value_array']
        # 利用sum函数将每一项进行相加
        result=sum([i['value'] for i in msg])
        return {"result":result}

class Get_date(Resource):
    def get(self):
        return {"date":time.strftime('%Y-%m-%d')}

class Chat(Resource):
    def post(self):
        body=json.loads(request.data)
        msg=body['msg']

        result=''
        if "您好" in msg:
            result = '您好，您吃了吗？'
        if "再见" in msg:
            result = '回见了您内。'

        pattern = re.compile('(再见).*(您好)')
        if len(pattern.findall(msg))>0:
            result = '天气不错。'
        return {"result":result}

api.add_resource(Add, '/add')
api.add_resource(Get_date, '/get_date')
api.add_resource(Chat, '/chat')

if __name__ == '__main__':
    app.run(debug=True)