# main.py: server에서 db와 소통할 수 있는 endpoint를 정의 및 가동.
# 실제 사용되는 HTTP method (get, post, put, delete)에 대한 처리 정의
# @app.get("/") decorator 문법 이용해 url 함수정의 가능.
# 실행 code: fastapi dev main.py --port portno
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models, crud, schemas
from rate_comments import CommentRater
import crud, models, schemas

models.Base.metadata.create_all(bind=engine) # db engine에 저장

app = FastAPI()

# Allow CORS for all origins (for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
# DB session 불러오기
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def read_root():
    return {"message": "Welcome to the Plant Comment API"}

# plant 생성하기. (plant 모델 스키마 안에 내용 채워넣기)
# 매개변수에 datatype 지정
@app.post("/plants/")
def create_plant(
    plant: schemas.PlantCreate, db: Session = Depends(get_db)
  ):
    return crud.create_plant_name_sort(db=db, plant=plant)

# comment 생성
# comment 생성하고, 해당 plant에 물 주기=> 계산은 어디서?
@app.post("/plants/comment/")
def comment_on_plant(
    comment: schemas.CommentCreate, db: Session = Depends(get_db)
  ):

  # comment instance 불러오기
  content = comment.comment_content
  comment_rater = CommentRater() # 인스턴스 생성 (API_KEY 불러오기)
  # 1. parsing: comment -> json 변경해 response에 저장.
  response = comment_rater.rate_comment(content)

  
  # 2. output 다루기 -> db 내 comment_score에 update (내부 동작 => input param 받을 필요없음)
  comment_score = sum(response.values()) # 총합 저장하기 -> score를 정수형태로 저장

  # 디버깅
  print(f"response: {response}")
  print(f"comment_score: {comment_score}")
    

  # comment_score도 업데이트하기
  return crud.create_comment_db(db=db, comment=comment, comment_score=comment_score)

    
@app.get("/plants/status/{plant_name}")
def get_plant_status(plant_name: str, db: Session = Depends(get_db)):
    return crud.get_plant_status(db=db, plant_name=plant_name)


@app.delete("/plants/status/{plant_name}")
def delete_plant(
  plant_name: str, db: Session = Depends(get_db)
  ):
    return crud.delete_plant_db(db=db, plant_name=plant_name)


@app.get("/plants/comments/{plant_name}")
def get_comments_by_plant(plant_name: str, db: Session = Depends(get_db)):
    return crud.get_comments_by_plant(db=db, plant_name=plant_name)

@app.get("/plants/all")
def get_all_plants(db: Session = Depends(get_db)):
    return crud.get_all_plants(db=db)

@app.get("/plants/growth_stage/{growth_stage}")
def get_plants_by_growth_stage(growth_stage: str, db: Session = Depends(get_db)):
    return crud.get_plants_by_growth_stage(db=db, growth_stage=growth_stage)

