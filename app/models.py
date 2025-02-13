from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import Enum
from app.database import Base
import enum

# TYPES
class CategoryEnum(enum.Enum):
    KARLKYNS = "karlkyns"
    KVENKYNS = "kvenkyns"
    KYNHLUTLAUS = "kynhlutlaust"
    MILLINOFN = "milli"


# DATABASE MODELS
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship with partner (another user)
    partner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    partner = relationship("User", remote_side=[id])
    
    # Relationships
    swipes = relationship("Swipe", back_populates="user")

class Name(Base):
    __tablename__ = "names"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(Enum(CategoryEnum), nullable=False)
    # origin = Column(String, nullable=True)
    # meaning = Column(String, nullable=True)
    
    # Relationships
    swipes = relationship("Swipe", back_populates="name")

class Swipe(Base):
    __tablename__ = "swipes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name_id = Column(Integer, ForeignKey("names.id"))
    liked = Column(Boolean)
    swiped_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="swipes")
    name = relationship("Name", back_populates="swipes")
