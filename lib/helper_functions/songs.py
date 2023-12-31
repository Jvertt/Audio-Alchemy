from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Artist, Song
from cli import pyfiglet

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

engine = create_engine("sqlite:///db/songs.db") 
session = Session(engine, future=True)

def create():
    title = input("Enter the title: ")
    artist_name = input("Enter the artist: ")
    album = input("Enter the album: ")
    genre = input("Enter the genre: ")
    duration = input("Enter the duration: ")

    artist = session.query(Artist).filter(Artist.name == artist_name).first()
    if artist is None:
        # Artist does not exist, create a new one
        artist = Artist(name=artist_name)
        session.add(artist)
        session.flush()  # Ensure the artist is assigned an ID

    new_song = Song(title=title, artist=artist, album=album, genre=genre, duration=duration)

    session.add(new_song)
    session.commit()
    print(f"Created song '{title}' successfully!")


def view():
    all_songs= session.query(Song).all()
    for songs in all_songs:
        print(f"Song ID: {songs.id}")
        print(f"Name: {songs.title}")
        print(f"Album: {songs.album}")
        print(f"Genre:{songs.genre}")
        print(f"Duration:{songs.duration} ")
        print()

def delete():
    all_songs= session.query(Song).all()
    for songs in all_songs:
        print(f"Song ID: {songs.id}")
        print(f"Name: {songs.title}")
        print(f"Album: {songs.album}")
        print(f"Genre:{songs.genre}")
        print(f"Duration:{songs.duration} ")
        print()
    
    id = input("Enter the ID of the song to delete: ")

    song = session.query(Song).get(id)

    if song:
        session.delete(song)
        session.commit()
        print("Song deleted successfully!")
    else:
        print("Song not found.")

def module():
    user_choice = 0
    while user_choice != 4:
        print(f'''

            Where would you like to go?
            ---------------------------
            1 - {Color.GREEN}Create Song{Color.RESET}

            2 - {Color.GREEN}View Songs{Color.RESET}

            3 - {Color.GREEN}Delete Song{Color.RESET}

            4 - {Color.RED}Back{Color.RESET}
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            create()
        elif user_choice == 2:
            view()
        elif user_choice == 3:
            delete()
        elif user_choice == 4:
            print('Going back to the main menu.')
        else:
            print("Invalid choice. Please try again.")