from app.database import Base
from sqlalchemy import Column, Integer, Text, String 
# table
class User(Base):
    # table name
    __tablename__ ="User_table"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    email = Column(String(350),unique=True, index=True)
    bio = Column(Text)