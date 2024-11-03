from pydantic import BaseModel

class UserAddDTO(BaseModel):
    username: str
    login: str
    password: str
    about_me: str | None

class UserDTO(UserAddDTO):
    id: int