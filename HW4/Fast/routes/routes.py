from fastapi import APIRouter, status
from .prods_parse import (
    get_pords_parse,
    get_pords_parse_id,
    get_pords_parse_name,
    post_pords_parse,
    put_pords_parse,
    delete_pords_parse,
)
from model.pords_model import Prod
from config.database import collection

from schemas.pords_schema import pords_serializer
from fastapi.responses import JSONResponse

pord_api_router = APIRouter()

# retrieve


@pord_api_router.get("/")
async def get_pords():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=get_pords_parse(),
    )


@pord_api_router.get("/{id}")
async def get_pord(id: str):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=get_pords_parse_id(id),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product id be " + id,
        )


@pord_api_router.get("/{id}/name")
async def pord_name_get(name: str):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=get_pords_parse_name(name),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product name has " + name,
        )


# post
@pord_api_router.post("/")
async def create_pord(pord: Prod):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=post_pords_parse(pord),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content="Creation failed",
        )


# update
@pord_api_router.put("/{id}")
async def update_pord(id: str, prod: Prod):
    try:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content=put_pords_parse(id, prod),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product id be " + id,
        )


# delete
@pord_api_router.delete("/{id}")
async def delete_pord(id: str):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=delete_pords_parse(id),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product id be " + id,
        )
