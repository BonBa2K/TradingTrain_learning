from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .prods_parse import *
from model.prods_model import Prod

prod_api_router = APIRouter()

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

@prod_api_router.get("/", tags=["basic"],response_model=Prod,responses=stdResponse)
async def get_prods_list():
    """
    一次性取得資料內所有資料
    """
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=get_prods_parse(),
    )


@prod_api_router.get("/{id}", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def get_prod(id: str):
    """
    根據id來搜尋並取得對應資料
    """
    try:
        output=get_prods_parse_id(id)
        if output!=[]:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=output,
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content="There is no product ID is " + id,
            )
    except:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=id + "is not an ObjectId",
            )

@prod_api_router.get("/{id}/name", tags=["function with name"],response_model=Prod,
    responses=stdResponse)
async def prod_name_get(name: str):
    """
    根據Name中是否有對應字符來搜尋並取得對應資料
    """
    try:
        output=get_prods_parse_name(name)
        if output!=[]:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=output,
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content="there is no product name has " + name,
            )
    except:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content="there is no product name has " + name,
            )


# post
@prod_api_router.post("/", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def create_prod(prod: Prod):
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
            content=post_prods_parse(prod),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content="Creation failed",
        )


# update
@prod_api_router.put("/{id}", tags=["basic"],response_model=Prod,
    responses=stdResponse)
async def update_prod(id: str, prod: Prod):
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
            content=put_prods_parse(id, prod),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product id be " + id,
        )


# delete
@prod_api_router.delete("/{id}", tags=["basic"])
async def delete_prod(id: str):
    """
    用id搜尋後刪除該資料
    """
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=delete_prods_parse(id),
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="there is no product id be " + id,
        )
