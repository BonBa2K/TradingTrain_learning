from config.database import collection
from bson import ObjectId

def Output_serializer(prods):
    Output = []
    for prod in prods:
        Output.append({
        "_id": str(prod["_id"]),
        "prod_name": prod["prod_name"],
        "prod_price": prod["prod_price"],
        "channel": prod["channel"],
        "created_at": prod["created_at"]
        })
    return Output
    
def get_prods_parse():
    prods=collection.find()
    return Output_serializer(prods)


def get_prods_parse_id(id_in):
    prods=collection.find({"_id": ObjectId(id_in)})
    return Output_serializer(prods)



def get_prods_parse_name(prod_name):
    prods=collection.find({"prod_name": {"$regex": prod_name}})
    return Output_serializer(prods)


def post_prods_parse(prod):
    _id = collection.insert_one(dict(prod))
    prods=collection.find({"_id": _id.inserted_id})
    return Output_serializer(prods)


def put_prods_parse(id_in, prod):
    collection.find_one_and_update({"_id": ObjectId(id_in)}, {"$set": dict(prod)})
    prods=collection.find({"_id": ObjectId(id_in)})
    return Output_serializer(prods)


def delete_prods_parse(id_in):
    try:
        collection.find_one_and_delete({"_id": ObjectId(id_in)})
        return {"status": "deleted"}
    except:
        return {"status": "delete fail"}