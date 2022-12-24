from config.database import collection
from bson import ObjectId
from schemas.pords_schema import pords_serializer


def get_pords_parse():
    return pords_serializer(collection.find())


def get_pords_parse_id(id_in):
    return pords_serializer(collection.find({"_id": ObjectId(id_in)}))


def get_pords_parse_name(prod_name):
    return pords_serializer(collection.find({"prod_name": {"$regex": prod_name}}))


def post_pords_parse(pord):
    _id = collection.insert_one(dict(pord))
    return pords_serializer(collection.find({"_id": _id.inserted_id}))


def put_pords_parse(id_in, pord):
    collection.find_one_and_update({"_id": ObjectId(id_in)}, {"$set": dict(pord)})
    return pords_serializer(collection.find({"_id": ObjectId(id_in)}))


def delete_pords_parse(id_in):
    collection.find_one_and_delete({"_id": ObjectId(id_in)})
    return {"status": "deleted"}
