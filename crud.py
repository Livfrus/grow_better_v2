from sqlalchemy.orm import Session
import models, schemas 
# from models import Plant, Comments
import uuid

def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email:str):
  return db.query(models.User).filter(models.User.email == email).first()

def get_users(db:Session, skip: int = 0, limit: int = 100):
  return db.query(models.USer).offset(skip).limit(limit).all()

def create_user_item(db: Session, item:schemas.ItemCreate, user_id: int):
  db_item = models.Item(**item.dict(), owner_id=user_id) # row 형태 준비 (넣을 아이템 준비)
  db.add(db_item)
  db.commit() # commit: 실질적 저장 단게
  db.refresh(db_item)
  return db_item

def create_user(db: Session, user:schemas.UserCreate, id: int):
  db_user = models.User(**user.dict(), id=id) # row 형태 준비 (넣을 아이템 준비)
  db.add(db_user)
  db.commit() # commit: 실질적 저장 단게
  db.refresh(db_user)
  return db_user

def delete_user(db: Session):
  obj = Session.query(models.User).filter_by(id=1).first()
  Session.delete(obj)
  Session.commit()