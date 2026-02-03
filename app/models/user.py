from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)  # 🔹 son login tarihi
    
    
    #CREATE TABLE users (
    #id SERIAL PRIMARY KEY,
    #email VARCHAR(255) UNIQUE NOT NULL,
    #is_active INTEGER DEFAULT 1,
    #created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    #last_login TIMESTAMP
    #);