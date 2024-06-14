# # sqlalchemy table 정의 script. 
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base, engine
import uuid

# '''

# DB Tables

# '''


# # class에서 Base 상속: DB인 sqlalchemy -> python class로 가져온다는 의미.
# class Plant(Base):
#     pass 

# class Comments(Base):
#     pass


# # Task: User, Info 모델 정의 pydantic -> SQLalchemy 형식으로 변경하기.
# class Info(Base):
#   __tablename__ = "infos"
#   # Question: primary key는 항상 첫 번쨰꺼?
#   course = Column(String, primary_key=True)
#   project = Column(String)

#   info_relation = relationship("User", back_populates="user_relation")

# class User(Base): 
#   __tablename__ = "users"
#   name = Column(String, primary_key=True)
#   age = Column(Integer)
#   email = Column(String, unique=True, index=True)
#   info = Column(String)

#   user_relation = relationship("Info", back_populates="info_relation")


# class User(Base):
#   __tablename__ = "users"
#   id = Column(Integer, primary_key=True)
#   email = Column(String, unique=True, index=True)
#   is_active = Column(Boolean, default=True)
  
#   items = relationship("Item", back_populates="owner")

# class Item(Base):
#   __tablename__ = "items"
#   id = Column(Integer, primary_key=True)
#   title = Column(String, index=True)
#   description = Column(String, index=True)
#   owner_id = Column(Integer, ForeignKey("users.id"))

#   owner = relationship("User", back_populates="items")
 
'''

DB Tables

'''
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="items")    
    
# Create all tables in the database
# 베이스로 넣어놓은 모든 클래스 생성, DB파일이 생성됨. DB 파일 생성하고싶으면 코드 무조건 있어야함. 
Base.metadata.create_all(bind=engine)
# Create all tables in the database
# test 할 때는 주석처리 해두어야 함 => 정의한 모델 클래스에 맞추어 DB생성하는 코드. 
# base로 만든 모든 DB가 생성됨 
# Base.metadata.create_all(bind=engine)
# 생성은 쉬우나, DB 업데이트가 안됨. DB 파일 자체를 지우고 재생