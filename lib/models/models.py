from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///anime.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Anime(Base):
    pass

#anime has many users
#anime has many reviews



class User(Base):
    pass
#user has many anime


class Review(Base):
    pass
#reviews belong to many users
