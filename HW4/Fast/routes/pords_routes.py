from fastapi import APIRouter

from model.pords_model import Prod
from config.database import collection

from schemas.pords_schema import pords_serializer, pord_serializer
from bson import ObjectId

pord_api_router = APIRouter()

# retrieve


@pord_api_router.get("/")
async def get_pords():
    pords = pords_serializer(collection.find())
    return pords


@pord_api_router.get("/{id}")
async def get_pord(id: str):
    Output = pords_serializer(collection.find({"_id": ObjectId(id)}))
    if (Output != []):
        return Output
    else:
        return "there is no product id be " + id


@pord_api_router.get("/{id}/name")
async def get_pord_name(name: str):
    Output = pords_serializer(collection.find({"prod_name": {"$regex": name}}))
    if (Output != []):
        return Output
    else:
        return "there is no product name has " + name


# post
@pord_api_router.post("/")
async def create_pord(pord: Prod):
    _id = collection.insert_one(dict(pord))
    return pords_serializer(collection.find({"_id": _id.inserted_id}))


# update
@pord_api_router.put("/{id}")
async def update_pord(id: str, pord: Prod):
    collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(pord)
    })
    return pords_serializer(collection.find({"_id": ObjectId(id)}))

# delete


@pord_api_router.delete("/{id}")
async def delete_pord(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
