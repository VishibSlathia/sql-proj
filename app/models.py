from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    queries = relationship("QueryHistory", back_populates="user")
    api_usage = relationship("APIUsage", back_populates="user")

class QueryHistory(Base):
    __tablename__ = "query_history"

    query_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    natural_language_query = Column(Text, nullable=False)
    generated_sql_query = Column(Text, nullable=False)
    execution_result = Column(Text)
    explanation = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="queries")

class APIUsage(Base):
    __tablename__ = "api_usage"

    usage_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    endpoint = Column(String(100), nullable=False)
    tokens_used = Column(Integer, nullable=False)
    cost = Column(DECIMAL(10, 4), nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="api_usage")