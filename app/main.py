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
    return {"Ég elska": "Ágústu"}


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


@app.get("/names")
def read_names():
    db = SessionLocal()
    names = db.query(models.Name).all()
    return names

@app.post("/populate_names")
def populate_names():
    db = SessionLocal()

    print("Starting to populate names")
    
    with open('names/kk.txt', 'r', encoding='utf-8') as file:
        male_names = file.read().splitlines()
        for name in male_names:
            db_name = models.Name(name=name, category=models.CategoryEnum.KARLKYNS)
            db.add(db_name)
        db.commit()
        print("Finished with male names")
        
    
    with open('names/kvk.txt', 'r', encoding='utf-8') as file:
        female_names = file.read().splitlines()
        for name in female_names:
            db_name = models.Name(name=name, category=models.CategoryEnum.KVENKYNS)
            db.add(db_name)
        db.commit()
        print("Finished with female names")

    with open('names/hvk.txt', 'r', encoding='utf-8') as file:
        neutral_names = file.read().splitlines()
        for name in neutral_names:
            db_name = models.Name(name=name, category=models.CategoryEnum.KYNHLUTLAUS)
            db.add(db_name)
        db.commit()
        print("Finished with neutral names")
    
    with open('names/milli.txt', 'r', encoding='utf-8') as file:
        middle_names = file.read().splitlines()
        for name in middle_names:
            db_name = models.Name(name=name, category=models.CategoryEnum.MILLINOFN)
            db.add(db_name)
        db.commit()
        print("Finished with middle names")
    
    return {"message": "Names populated"}