from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True  # This allows SQLAlchemy models to be converted to Pydantic models
