from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///anime.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Anime(Base):

    __tablename__ = 'animes'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    description = Column(String())
    genre = Column(String())
    episode_count = (Integer())
    watched = Column(Boolean)
    status = Column(String())

    reviews = relationship('Review', backpopulates='animes')
    users = relationship('Users', backpopulates='animes')

# anime has many users
# anime has many reviews


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    susername = Column(String())
    email = Column(String())
    favorite_anime = Column(String())


# user has many anime
    anime_id = relationship(Integer(), ForeignKey('animes.id'))


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(),primary_key=True)
    
    rating = Column(String())
    comment = Column(String())
# reviews belong to many users
    
    anime_id = relationship(Integer(),ForeignKey('animes.id'))
    user_id=relationship(Integer(),ForeignKey('users.id'))
