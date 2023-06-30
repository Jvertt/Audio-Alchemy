from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

song_playlist_association = Table(
    'song_playlist_association',
    Base.metadata,
    Column('song_id', Integer, ForeignKey('songs.id')),
    Column('playlist_id', Integer, ForeignKey('playlists.id'))
)

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    album = Column(String(255))
    genre = Column(String(255))
    duration = Column(Integer)

    artist = relationship("Artist", backref=backref('songs'))
    playlists = relationship("Playlist", secondary=song_playlist_association, backref='songs')

    def __repr__(self):
        return f'<Song(id={self.id}, title="{self.title}", artist_id={self.artist_id}, album="{self.album}", genre="{self.genre}", duration={self.duration})>'

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))

    def __repr__(self):
        return f'<Playlist(id={self.id}, name="{self.name}", description="{self.description}")>'


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    bio = Column(String(255))

    def __repr__(self):
        return f'<Artist(id={self.id}, name="{self.name}", bio="{self.bio}")>'


if __name__ == '__main__':
    print("Welcome")
    print("Come Back Again!")
