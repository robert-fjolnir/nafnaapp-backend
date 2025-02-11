from fastapi import FastAPI, Depends
from app import models
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def read_users():
    db = SessionLocal()
    users = db.query(models.User).all()
    return users

@app.post("/users")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    db = SessionLocal()
    db_user = models.User(email=email, hashed_password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user