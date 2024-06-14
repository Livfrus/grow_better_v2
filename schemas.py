from pydantic import BaseModel

'''

Pydantic Data Validation Schemas (Response and Request)

'''

class ItemBase(BaseModel):
  title: str
  description: str | None = None

class ItemCreate(ItemBase):
  pass