from database import *
from Schemas import *
from models import *


class UserRepository:
    @classmethod
    def add_user(cls, data: UserDTO) -> int:
        with session_factory() as session:
            try:
                user_dict = data.model_dump()
                user = User(**user_dict)
                session.add(user)
                session.flush()
                session.commit()
                return user.id
            except IntegrityError:
                session.rollback()
                print(f'This user is already registered')

    @classmethod
    def get_all_users(cls) -> list:
        with session_factory() as session:
            try:
                query = (
                    select(User)
                )
                result = session.execute(query).scalars().all()
                return result
            except Exception as e:
                print(e)

    @classmethod
    def delete_user(cls, user_d: int) -> int:
        with session_factory() as session:
            try:
                query = (
                    select(User)
                    .where(User.id == user_d)
                )
                result = session.execute(query).scalars().first()
                if not result:
                    session.rollback()
                    print(f'This user is not registered')
                session.delete(result)
                session.commit()
                return result.id
            except Exception as e:
                print(e)

    @classmethod
    def update_user_password(cls, user_d: int, new_password: str) -> int:
        with session_factory() as session:
            try:
                query = (
                    select(User)
                    .where(User.id == user_d)
                )
                result = session.execute(query).scalars().first()
                if not result:
                    session.rollback()
                    print(f'This user is not registered')
                result.password = new_password
                session.commit()
                return result.id
            except Exception as e:
                print(e)

