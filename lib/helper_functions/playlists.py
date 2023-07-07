from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Playlist, Song
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
        print("Songs:")
        for song in playlist.songs:
            print(f" - {song.title} by {song.artist.name}")
        print()

def add_song_to_playlist():
    all_playlists = session.query(Playlist).all()
    for playlist in all_playlists:
        print(f"Playlist ID: {playlist.id}")
        print(f"Name: {playlist.name}")
        print()

    playlist_id = input("Enter the ID of the playlist: ")

    all_songs= session.query(Song).all()
    for songs in all_songs:
        print(f"Song ID: {songs.id}")
        print(f"Name: {songs.title}")
        print()

    song_id = input("Enter the ID of the song: ")

    playlist = session.query(Playlist).get(playlist_id)
    song = session.query(Song).get(song_id)

    if playlist and song:
        playlist.songs.append(song)
        session.commit()
        print(f"Added song '{song.title}' to playlist '{playlist.name}' successfully!")
    else:
        print("Playlist or song not found.")

def delete():
    all_playlists = session.query(Playlist).all()
    for playlist in all_playlists:
        print(f"Playlist ID: {playlist.id}")
        print(f"Name: {playlist.name}")
        print(f"Description: {playlist.description}")
        print()

    id = input("Enter the ID of the playlist to delete: ")

    playlist = session.query(Playlist).get(id)

    if playlist:
        session.delete(playlist)
        session.commit()
        print("Playlist deleted successfully!")
    else:
        print("Playlist not found.")

def module():
    user_choice = 0
    while user_choice != 5:
        print(f'''
            Where would you like to go?
            ---------------------------
            1 - {Color.GREEN}Create playlist{Color.RESET}

            2 - {Color.GREEN}View Playlist{Color.RESET}

            3 - {Color.GREEN}Add Song To Playlist{Color.RESET}

            4 - {Color.GREEN}Delete Playlist{Color.RESET}

            5 - {Color.RED}Back{Color.RESET}
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            create()
        elif user_choice == 2:
            view()
        elif user_choice == 3:
            add_song_to_playlist()
        elif user_choice == 4:
            delete()
        elif user_choice == 5:
            print('Going back to the main menu.')
        else:
            print("Invalid choice. Please try again.")