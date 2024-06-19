# schemas.py => for data validation
# 즉, data 검증을 위해서 '직접' 사용자에게 입력받을 것들. 자동생성되는 것은 검증되므로 작성할 필요 X.
# 출력 부분에 대한 추가적인 코딩 -> 원래 DB의 것이 아닌 것...
from pydantic import BaseModel
import uuid
from typing import Optional


'''

Pydantic Data Validation Schemas (Response and Request)

'''

# 데이터 검증 -> 사용자와 직접 소통할 필요있는 변수들만 이용.
# 응답 데이터에서 필요한 필드만 '선택'해 클라이언트에 반환.
class Plant(BaseModel):
# input value 말고 기본 값들 잡아주기.
  plant_name: str
  growth_stage: str
  sort: str
  plant_score: int
# 기본 모델 구조 상속받기-> 그냥 practice가 그래.
class PlantCreate(Plant):
  pass

class Comment(BaseModel):
  comment_content: str
  comment_score: int # 변환할 값 (기본값 0)
  plant_to_comment: str

# 기본 모델 구조 상속받기
class CommentCreate(Comment):
  pass