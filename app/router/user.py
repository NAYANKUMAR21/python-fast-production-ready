from fastapi import APIRouter, Depends, status, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.crud.user import (getAllUser, create_User, updateUser, delete_user)
from app.schema.user import UserCreate, UserResponse, UserUpdate

router=APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def getUsers(db:Session=Depends(get_db)):
    db_all_user =getAllUser(db)
    return db_all_user

    
@router.post("/",response_model=UserResponse)
def create_user(user_data:UserCreate, db:Session=Depends(get_db)):
    return create_User(db, user_data)


@router.patch("/{user_id}",response_model=UserResponse)
def update_user_feild(user_id:int, user_data:UserUpdate, db:Session=Depends(get_db)):
    return updateUser(db, user_id, user_data)



@router.delete("/{user_id}")
def delete_user_id(user_id:int, db:Session=Depends(get_db)):
    return delete_user(db, user_id)
