from pydantic import BaseModel

'''

Pydantic Data Validation Schemas (Response and Request)

'''

class ItemBase(BaseModel):
  title: str
  description: str | None = None

class ItemCreate(ItemBase):
  pass

class UserBase(BaseModel): # 여기서 정의한 두가지는 모두 사용자에게 직접 받아올 것들.
  email: str
  is_active: bool

class UserCreate(UserBase):
  pass

class UserDelete(UserBase):
  pass