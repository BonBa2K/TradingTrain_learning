from fastapi import APIRouter, status
from .prods_parse import (
    get_pords_parse,
    get_pords_parse_id,
    get_pords_parse_name,
    post_pords_parse,
    put_pords_parse,
    delete_pords_parse
)
from model.pords_model import Prod
from fastapi.responses import JSONResponse
from pydantic import BaseModel

pord_api_router = APIRouter()

# retrieve
class Message(BaseModel):
    message: str

stdResponse={
        200: {
            "description": "Item requested by ID",
            "content": {
                "application/json": {
                    "example": {
                                "_id": {
                                    "$oid": "63b3ea1723a1b15b742ae160"
                                },
                                "prod_name": "SAMSUNG三星 43吋4K HDR QLED量子智慧連網電視(QA43Q60BAWXZW)",
                                "prod_price": 24210,
                                "channel": "PChome",
                                "created_at": "2023-01-03T16:40:54Z"
                                }
                }
            },
        },
    }

@pord_api_router.get("/", tags=["basic"],response_model=Prod,responses=stdResponse)
async def get_pords_list():
    """
    一次性取得資料內所有資料
    """
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=get_pords_parse(),
    )


@pord_api_router.get("/{id}", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def get_pord(id: str):
    """
    根據id來搜尋並取得對應資料
    """
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


@pord_api_router.get("/{id}/name", tags=["function with name"],response_model=Prod,
    responses=stdResponse)
async def pord_name_get(name: str):
    """
    根據Name中是否有對應字符來搜尋並取得對應資料
    """
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
@pord_api_router.post("/", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def create_pord(pord: Prod):
    """
    創建屬於自己的新資料
    - **prod_name**: 商品名稱
    - **prod_price**: 商品價格
    - **channel**: 資料來源平台
    - **created_at**: 資料創建時間
    """
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
@pord_api_router.put("/{id}", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def update_pord(id: str, prod: Prod):
    """
    用id搜尋後依照輸入內容更新該資料
    - **prod_name**: 商品名稱
    - **prod_price**: 商品價格
    - **channel**: 資料來源平台
    - **created_at**: 資料創建時間
    """
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
@pord_api_router.delete("/{id}", tags=["basic"])
async def delete_pord(id: str):
    """
    用id搜尋後刪除該資料
    """
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
