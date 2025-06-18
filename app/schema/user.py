from pydantic import BaseModel, Field, EmailStr,constr
class UserCreate(BaseModel):
    name:str= Field(..., min_length=3, max_length=100)
    email:EmailStr = Field(..., example="johndoe@gmail.com", description="Please add email only" )
    bio:constr(max_length=500) | None = Field(None,example="Something about myself",
        description="Optional user biography")
    




class UserUpdate(BaseModel):
    name:str | None = Field(None, min_length=3, max_length=100)
    email:EmailStr| None = Field(None, example="johndoe@gmail.com", description="Please add email only" )
    bio:constr(max_length=500) | None = Field(None,example="Something about myself",
        description="Optional user biography")


class UserResponse(BaseModel):
    id: int
    class config:
        from_attributes=True