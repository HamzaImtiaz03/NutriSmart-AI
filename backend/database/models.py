from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .db import Base

class MealLog(Base):
    __tablename__ = 'meal_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    meal = Column(String)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
