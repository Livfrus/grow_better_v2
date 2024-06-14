# # sqlalchemy table 정의 script. 
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base, engine
import uuid
from datetime import datetime

'''

DB Tables

'''

# class에서 Base 상속: DB인 sqlalchemy -> python class로 가져온다는 의미.
class Plant(Base):
  __tablename__ = "plants"

  id = Column(Integer, primary_key=True) 
  plant_name = Column(String, unique=True) # 이름은 고유값
  growth_stage = Column(String, index=True) # 정렬 가능한 string (lv1, 2, 3)
  sort = Column(String, index=True) # 정렬 가능한 string (A, B, C)
  plant_score = Column(Integer) # 누적할 점수값
  
  comment_plant = relationship("Comments", back_populates="comments")


class Comment(Base):
  __tablename__ = "comments"

  id = Column(Integer, primary_key=True) # id 고유값
  comment_score = Column(Integer) # 변환할 값
  comment_time = Column(datetime) # 날짜와 시간 => 확인 필요
  plant_to_comment = Column(String, ForeignKey("plants.id")) # 어떤 대상으로 연결할지: plant의 id로 연결.

  plant_comment = relationship("Plant", back_populates="plants")

# Create all tables in the database
# 베이스로 넣어놓은 모든 클래스 생성, DB파일이 생성됨. DB 파일 생성하고싶으면 코드 무조건 있어야함. 
Base.metadata.create_all(bind=engine)
# Create all tables in the database
# test 할 때는 주석처리 해두어야 함 => 정의한 모델 클래스에 맞추어 DB생성하는 코드. 
# base로 만든 모든 DB가 생성됨 
# Base.metadata.create_all(bind=engine)
# 생성은 쉬우나, DB 업데이트가 안됨. DB 파일 자체를 지우고 재생