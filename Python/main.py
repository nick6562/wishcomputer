# from enum import Enum
from pydoc import describe
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price = float
    tax: Optional[float] = None


app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
#     if model_name == ModelName.lenet:
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name": model_name, "message": "Never some residuals"}

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# @app.get("/items/")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

@app.get("/items/")
async def create_item(item: Item):
    return item