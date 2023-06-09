import os
import sqlalchemy as sa
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

# Set the logging level to suppress SQLAlchemy logs
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

Base = declarative_base()
engine = create_engine('sqlite:///anime.db')
Session = sessionmaker(bind=engine)
session = Session()



# Disable SQLAlchemy logging
logging.getLogger(sa.__name__).setLevel(logging.ERROR)
class Anime(Base):
    __tablename__ = 'animes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    genre = Column(String)
    episode_count = Column(Integer)
    status = Column(String)
    watched = Column(Boolean)

    # Specify the back_populates parameter to resolve the conflicts
    users = relationship('User', back_populates='favorite_anime')
    reviews = relationship('Review', back_populates='anime')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    favorite_anime_id = Column(Integer, ForeignKey('animes.id'))

    # Specify the back_populates parameter to resolve the conflicts
    favorite_anime = relationship('Anime', back_populates='users')
    reviews = relationship('Review', back_populates='user')


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    anime_id = Column(Integer, ForeignKey('animes.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Specify the back_populates parameter to resolve the conflicts
    anime = relationship('Anime', back_populates='reviews')
    user = relationship('User', back_populates='reviews')

Base.metadata.create_all(engine)