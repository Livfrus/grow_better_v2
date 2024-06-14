# schemas.py => for data validation
# 즉, data 검증을 위해서 '직접' 사용자에게 입력받을 것들. 자동생성되는 것은 검증되므로 작성할 필요 X.
from pydantic import BaseModel
import uuid

'''

Pydantic Data Validation Schemas (Response and Request)

'''

# 사용자에게 직접 안 받아올 것들만 작성 (필터링 할 것만 작성)
class Plant(BaseModel):
# input value 말고 기본 값들 잡아주기.
  id: str = uuid.uuid4()
  growth_stage: str 
  plant_score: int
# 기본 모델 구조 상속받기
class PlantCreate(Plant):
  pass

class Comment(BaseModel):

  id: str = uuid.uuid4()
  comment_score: int # 변환할 값 (기본값 0)

# 기본 모델 구조 상속받기
class CommentCreate(Comment):
  pass