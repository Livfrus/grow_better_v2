# Models: 최종적으로 DB에 저장되는 Schema (테이블 형식 정의하기)
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base, engine
import uuid # unique ID 직접 만들어주는 모듈.
# from datetime import datetime

'''

DB Tables

'''

# class에서 Base 상속: DB인 sqlalchemy -> python class로 가져온다는 의미.
class Plant(Base):
  __tablename__ = "plants"

  id = Column(String, primary_key=True)  # uuid? 
  plant_name = Column(String, unique=True) # 이름은 고유값
  growth_stage = Column(String, index=True, default="lv1") # 정렬 가능한 string (lv1, 2, 3)
  sort = Column(String, index=True) # 정렬 가능한 string (A, B, C)
  plant_score = Column(Integer, default=0) # 누적할 점수값
  
  comment_plant = relationship("Comment", back_populates="plant_comment")


class Comment(Base):
  __tablename__ = "comments"

  id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4())) # id 고유값
  comment_content = Column(String) # comment 내용
  comment_score = Column(Integer, default=0) # 변환할 값 (기본값 0)
  # comment_time = Column(String) # 날짜와 시간 => 확인 필요
  plant_to_comment = Column(String, ForeignKey("plants.id")) # 어떤 대상으로 연결할지: plant의 id로 연결.

  plant_comment = relationship("Plant", back_populates="comment_plant")

# Create all tables in the database
# 베이스로 넣어놓은 모든 클래스 생성, DB파일이 생성됨. DB 파일 생성하고싶으면 코드 무조건 있어야함. 
Base.metadata.create_all(bind=engine)
# Create all tables in the database
# test 할 때는 주석처리 해두어야 함 => 정의한 모델 클래스에 맞추어 DB생성하는 코드. 
# base로 만든 모든 DB가 생성됨 
# Base.metadata.create_all(bind=engine)
# 생성은 쉬우나, DB 업데이트가 안됨. DB 파일 자체를 지우고 재생