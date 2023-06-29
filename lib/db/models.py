from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()
 
class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    album = Column(String(255))
    genre = Column(String(255))
    duration = Column(Integer)

    artist = relationship("Artist", backref=backref('songs'))

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    bio = Column(String(255))


if __name__ == '__main__':
    print("Welcome")
    print("Come Back Again!")