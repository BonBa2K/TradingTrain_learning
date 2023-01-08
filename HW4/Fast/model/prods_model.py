from pydantic import BaseModel, Field


class Prod(BaseModel):
    _id: str = Field(title="商品ID")
    prod_name: str = Field(title="商品名稱")
    prod_price: int = Field(title="商品價格")
    channel: str = Field(title="所在平台")
    created_at: str = Field(title="資料創建時間")
