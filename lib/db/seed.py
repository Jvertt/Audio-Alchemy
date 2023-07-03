from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
import random

from models import Song, Playlist, Artist

faker = Faker()

engine = create_engine("sqlite:///songs.db")
Session = sessionmaker(bind=engine)
session = Session()

# Clear data when session runs
session.query(Song).delete()
session.query(Playlist).delete()
session.query(Artist).delete()

def seed_data():
    # Generate artist data
    artists = []
    for i in range(5):
        artist = Artist(
            name=faker.name(),
            bio=faker.paragraph()
        )
        artists.append(artist)

    # Generate song data
    songs = []
    for i in range(10):
        artist = random.choice(artists)
        song = Song(
            title=faker.word(),
            artist=artist,
            album=faker.word(),
            genre=faker.word(),
            duration=faker.random_int(min=180, max=300)
        )
        songs.append(song)

    # Generate playlist data
    playlists = []
    for i in range(3):
        playlist = Playlist(
            name=faker.word(),
            description=faker.sentence()
        )
        playlists.append(playlist)

    # Add songs to playlists
    for playlist in playlists:
        playlist.songs.extend(random.choices(songs, k=5))

    # Add all data to the session
    session.add_all(artists + songs + playlists)
    session.commit()
    print("Data seeding completed successfully.")
    
if __name__ == '__main__':
    seed_data()