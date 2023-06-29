from faker import Faker 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Song, Playlist, Artist 

engine = create_engine('sqlite:///music_library.db')
Session = sessionmaker(bind=engine)

faker = Faker()

def seed_data():
    session = Session()

    #artists
    for i in range(5):
        name = faker.name()
        bio = faker.paragraph()
        artist = Artist(name=name, bio=bio)
        session.add(artist)
    
    session.commit()

    session.close()
    print("Data seeding completed successfully.")

if __name__ == '__main__':
    seed_data()