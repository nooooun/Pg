from Schemas import *
from repository import UserRepository
from fastapi import APIRouter, Depends
from typing import Annotated

router = APIRouter(
    prefix="/users",
    tags =["Users"],
)

@router.post("")
def add_user(user: Annotated[UserAddDTO, Depends()]):
    UserRepository.add_user(user)
    return {"message": "User added successfully"}

@router.get("")
def get_users():
    users = UserRepository.get_all_users()
    return {"users": users}

@router.delete("")
def delete_user(user_id: int):
    UserRepository.delete_user(user_id)
    return {"message": "User deleted successfully"}

@router.put("")
def update_user(user_id: int, new_password: str):
    UserRepository.update_user_password(user_id, new_password)
    return {"message": "User updated successfully"}