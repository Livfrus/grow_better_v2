from sqlalchemy.orm import Session
from . import models, schemas # 같은 폴더에 있는거 (같은 경로)
from models import Plant, Comments
import uuid

def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
  return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int=100):
  return db.query(models.User).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
  # models: ORM에서 정의한 class. 
  # commit하지 않은 행의 값들. 
  db_item = models.Item(**item.dict(), owner_id = user_id) # row 형태 준비 (넣을 아이템 준비)
  db.add(db_item) # 한 번 넣어본거
  db.commit() # commit: 저장 단게
  db.refresh(db_item) # db refresh => 넣었다고 출력하기
  return db_item