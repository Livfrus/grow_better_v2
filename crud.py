# DB에 접근해 CRUD 작업을 처리하는 함수를 정의. (실제 db와 소통하는 역할?)
# 추후 main.py에서 이 함수들을 호출해 실제 작업을 수행 (실제 db 잡아 갱신)
from sqlalchemy.orm import Session
import models, schemas 
# from models import Plant, Comments
import uuid

# plant DB 생성
def create_plant_name_sort(db: Session, plant: schemas.PlantCreate):
    db_plant = models.Plant(**plant.dict())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant

# comment DB 생성 => 함수의 parameter로 잡지 않기. 파라미터로 불러오면 그거댐
def create_comment_db(db: Session, comment: schemas.CommentCreate, comment_score:int):
  db_comment = models.Comment(**comment.dict()) # row 형태 준비 (넣을 아이템 준비) -> schema 전체 가져오기
  
  db_comment.comment_score = comment_score
  # comment_score 내서 plant_score에 누적 저장시키기.
  db_plant = db.query(models.Plant).filter(models.Plant.plant_name == db_comment.plant_to_comment).first() # plant_to_comment랑 같은 이름인 식물 객체 불러오기
  
  if db_plant: # 찾은 경우
    db_plant.plant_score += comment_score
    
    # growth_stage 업데이트 로직 추가
    if db_plant.plant_score < 15: # 0-15: lv1
        db_plant.growth_stage = "lv1"
    elif db_plant.plant_score < 30: # 15-30: lv2
        db_plant.growth_stage = "lv2"
    else:
        db_plant.growth_stage = "lv3" # 30 이상: lv3
            
    db.add(db_plant)
  
  db.add(db_comment)
  db.commit() # commit: 실질적 저장 단게
  db.refresh(db_comment)
  # db.refresh(db_plant)
  return db_comment

# def get_plant_status_db(db: Session, )

def delete_plant_db(db: Session, plant_name: str):
  obj = db.query(models.Plant).filter_by(plant_name=plant_name).first()
  db.delete(obj) # session에서 object를 지우기.
  db.commit()
  
def get_plant_status(db: Session, plant_name: str):
  return db.query(models.Plant).filter(models.Plant.plant_name == plant_name).all()

def get_comments_by_plant(db: Session, plant_name: str):
    return db.query(models.Comment).filter_by(plant_to_comment=plant_name).all()

def get_all_plants(db: Session):
    return db.query(models.Plant).all()

def get_plants_by_growth_stage(db: Session, growth_stage: str):
    return db.query(models.Plant).filter(models.Plant.growth_stage == growth_stage).all()
  