from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import Base

engine = create_engine("sqlite:///sigab.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
