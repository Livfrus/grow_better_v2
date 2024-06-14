# main 함수 정의: server에서 db와 소통할 수 있는 endpoint를 정의 및 가동.
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models, crud, schemas
from rate_comments import CommentRater
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

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
@app.post("/plants/")
def create_plant(
    plant_name: str, sort: str, plant: schemas.PlantCreate, db: Session = Depends(get_db)
  ):
    return crud.create_plant_name_sort(db=db, plant=plant, plant_name=plant_name, sort=sort)

@app.post("/plants/comment/")
def comment_on_plant(
    comment: schemas.CommentCreate,  comment_content: str, plant_to_comment: str, db: Session = Depends(get_db)
  ):
  return crud.create_comment_db(db=db, comment=comment, comment_content=comment_content, plant_to_comment=plant_to_comment)

    
@app.get("/plants/status/{plant_name}", response_model=schemas.Plant)
def get_plant_status(plant_name: str, db: Session = Depends(get_db)):
    pass


@app.delete("/plants/status/{plant_name}")
def delete_plant(plant_name: str, db: Session = Depends(get_db)):
    pass

@app.get("/plants/comments/{plant_name}", response_model=list[schemas.Comment])
def get_comments_by_plant(plant_name: str, db: Session = Depends(get_db)):
    pass

@app.get("/plants/all", response_model=list[schemas.Plant])
def get_all_plants(db: Session = Depends(get_db)):
    pass

@app.get("/plants/growth_stage/{growth_stage}", response_model=list[schemas.Plant])
def get_plants_by_growth_stage(growth_stage: str, db: Session = Depends(get_db)):
    pass

