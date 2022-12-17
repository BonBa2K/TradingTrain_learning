import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['demoDB']
data = myclient['demoDB']["users"]



print('data.find() = ', data.find_one( {'prod_price': 24900}))
