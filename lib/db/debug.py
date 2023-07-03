from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Artist, Song, Playlist)

if __name__ == '__main__':
    engine = create_engine("sqlite:///songs.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()