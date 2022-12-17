#!/usr/bin/python3
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['demoDB']
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
data = mydb["users"]

mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
z = data.delete_many({})
x = data.insert_many(mylist)
y = data.insert_one(mydict)
print(x.inserted_ids)
print(y.inserted_id)
print(z.deleted_count, "个文档已删除")