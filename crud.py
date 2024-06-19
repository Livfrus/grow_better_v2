# DB에 접근해 CRUD 작업을 처리하는 함수를 정의. (실제 db와 소통하는 역할?)
# 추후 main.py에서 이 함수들을 호출해 실제 작업을 수행 (실제 db 잡아 갱신)
from sqlalchemy.orm import Session
import models, schemas 
# from models import Plant, Comments
import uuid

# plant DB 생성
def create_plant_name_sort(db: Session, plant: schemas.PlantCreate, plant_name: str, sort: str):
    db_plant = models.Plant(plant_name=plant_name, sort=sort)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant

# comment DB 생성
def create_comment_db(db: Session, comment: schemas.CommentCreate, comment_content: str, plant_to_comment: str):
  db_comment = models.Comment(comment_content=comment_content, plant_to_comment=plant_to_comment) # row 형태 준비 (넣을 아이템 준비) -> plant schema 전체 가져오기
  db.add(db_comment)
  db.commit() # commit: 실질적 저장 단게
  db.refresh(db_comment)
  return db_comment

# plant, comment DB 생성까지는 완료. 이제 다른애들을 어떻게 다루지?
# def get_plant_status_db(db: Session, )

def delete_plant_db(db: Session, plant_name: str):
  obj = db.query(models.Plant).filter_by(plant_name=plant_name).first()
  db.delete(obj) # session에서 object를 지우기.
  db.commit()
  
def get_plant_status(db: Session, plant_name: str):
  return db.query(models.Plant).filter_by(plant_name=plant_name).first()

def get_comments_by_plant(db: Session, plant_name: str):
    return db.query(models.Comment).filter_by(plant_to_comment=plant_name).all()

def get_all_plants(db: Session):
    return db.query(models.Plant).all()

def get_plants_by_growth_stage(db: Session, growth_stage: str):
    return db.query(models.Plant).filter(models.Plant.growth_stage == growth_stage).all()
  

