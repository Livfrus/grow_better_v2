# schemas.py => for data validation
from pydantic import BaseModel

'''

Pydantic Data Validation Schemas (Response and Request)

'''

class PlantBase(BaseModel):
  pass

class PlantCreate(PlantBase):
  pass

class CommentBase(BaseModel):
  pass

class CommentCreate(CommentBase):
  pass