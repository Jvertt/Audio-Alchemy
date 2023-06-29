from faker import Faker 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Song, Playlist, Artist 

engine = create_engine('sqlite:///music_library.db')
Session = sessionmaker(bind=engine)