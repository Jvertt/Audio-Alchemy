from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Artist
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
    name = input("Enter the artist's name: ")

    new_name = Artist(name=name)

    session.add(new_name)
    session.commit()
    print(f"Artist '{name}' created successfully!")

def view():
    all_artists = session.query(Artist).all()
    for artist in all_artists:
        print(f"Artist ID: {artist.id}")
        print(f"Name: {artist.name}")
        print()

def delete():
    all_artists = session.query(Artist).all()
    for artist in all_artists:
        print(f"Artist ID: {artist.id}")
        print(f"Name: {artist.name}")
        print()

    artist_id = input("Enter the ID of the artist to delete: ")

    artist = session.query(Artist).get(artist_id)

    if artist:
        session.delete(artist)
        session.commit()
        print("Artist deleted successfully!")
    else:
        print("Artist not found.")

def module():
    user_choice = 0
    while user_choice != 4:
        print(f'''

            Where would you like to go?
            ---------------------------
            1 - {Color.GREEN}Create Artist{Color.RESET}

            2 - {Color.GREEN}View Artists{Color.RESET}

            3 - {Color.GREEN}Delete Artist{Color.RESET}

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
