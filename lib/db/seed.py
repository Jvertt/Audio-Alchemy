from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Song, Playlist, Artist


engine = create_engine("sqlite:///db/songs.db")
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

def seed_data():
    session = Session()

    # Seed artists
    for _ in range(5):
        name = faker.name()
        bio = faker.paragraph()
        artist = Artist(name=name, bio=bio)
        session.add(artist)

    session.commit()

    # Seed songs
    artists = session.query(Artist).all()
    for _ in range(10):
        title = faker.word()
        artist = faker.random.choice(artists)
        album = faker.word()
        genre = faker.word()
        duration = faker.random_int(min=180, max=300)
        song = Song(title=title, artist=artist, album=album, genre=genre, duration=duration)
        session.add(song)

    session.commit()

    # Seed playlists
    songs = session.query(Song).all()
    for _ in range(3):
        name = faker.word()
        description = faker.sentence()
        playlist = Playlist(name=name, description=description)

        # Add random songs to the playlist
        playlist.songs.extend(faker.random_choices(songs, length=5))
        
        session.add(playlist)

    session.commit()

    session.close()
    print("Data seeding completed successfully.")

if __name__ == '__main__':
    seed_data()
