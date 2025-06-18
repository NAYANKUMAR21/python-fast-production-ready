from sqlalchemy.orm import Session
from app.model.user import User



def getAllUser(db:Session):
    all_users = db.query(User).all()
    return all_users


def create_User(db:Session, user_data):
    db_user = User(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # it is like getting the item 
    return db_user


def updateUser(db:Session, user_id:int, user_update_data):
    db_user = db.query(User).filter(User.id==user_id).first()
    if db_user:
        update_data = user_update_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        
        db.commit()
        db.refresh(db_user)

    return db_user





def delete_user(db:Session, user_id:int):
    db_user = db.query(User).filter(User.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
        # db.refresh()
    return False


