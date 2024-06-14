# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. DB URL: DB server가 있는 경우, URL을 통해서 서버로 접근하게 된다 (작으면 파일인데 좀 크면 서버 됨)
# web에서 사용할 거면 로컬로 못 두니까 => 외부의 DB 접속할수 있게끔. 
DATABASE_URL = "sqlite:///./growbetter.db"  # SQLite for simplicity

# 2. Engine: server connect 용 engine. 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 통신용 통로 (session) 만드는 친구
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# table 만들기 위한 도구 (기본 선언문)
Base = declarative_base()

