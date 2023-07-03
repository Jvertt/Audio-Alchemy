from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Artist

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
        print('''
            Where would you like to go?
            1 - Create artist
            2 - View artists
            3 - Delete artist
            4 - back
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
