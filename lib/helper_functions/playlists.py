from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Artist, Playlist, Song

engine = create_engine("sqlite:///db/songs.db") 
session = Session(engine, future=True)

def create():
    name = input("Enter the name: ")
    description = input("Enter the description: ")

    new_playlist = Playlist(name=name, description=description)
    session.add(new_playlist)
    session.commit()

    print(f"Created {name} successfully!")

def view():
    all_playlists = session.query(Playlist).all()
    for playlist in all_playlists:
        print(f"Playlist ID: {playlist.id}")
        print(f"Name: {playlist.name}")
        print(f"Description: {playlist.description}")
        print()

def delete():
    all_playlists = session.query(Playlist).all()
    for playlist in all_playlists:
        print(f"Playlist ID: {playlist.id}")
        print(f"Name: {playlist.name}")
        print(f"Description: {playlist.description}")
        print()

    id = input("Enter the ID of the entity to delete: ")

    playlist = session.query(Playlist).get(id)

    if playlist:
        session.delete(playlist)
        session.commit()
        print("Playlist deleted successfully!")
    else:
        print("Playlist not found.")

def module():
    user_choice = 0
    while user_choice != 4:
        print('''
         Where would you like to go?
            1 - Create playlist
            2 - View playlists
            3 - Delete playlist
            4 - Back
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