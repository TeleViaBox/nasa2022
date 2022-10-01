#!/bin/python3
#### credit: https://vocus.cc/article/626f67e4fd89780001be4f3a
# 載入Flask套件
from flask import Flask
# 載入Flask RestFul 套件
from flask_restful import Api, Resource
# 創建Flask app物件
app = Flask(__name__)
# 創建Flask api物件
api = Api(app)
# 創建 output 範例內容
output = [
    {
        "pid": "1",
        "title": "Example01",
        "price": 10,
        "img": "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]
# 創建Products 物件並繼承Resource物件
class Products(Resource):
    def get(self):
        return {"products": {"Message": "Get all products..", "output": output}}, 200
# 建立API路由products，並將該路由導向Products物件
api.add_resource(Products, '/products')
if __name__ == "__main__":
    app.run(port=8088, debug=True)
