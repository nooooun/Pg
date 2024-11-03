from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, joinedload, selectinload
from sqlalchemy.exc import IntegrityError


DATABASE_URL = 'sqlite:///Lab_rest_api.db'

engine = create_engine(
    url=DATABASE_URL
    )

session_factory = sessionmaker(bind=engine)