import sys
import importlib
sys.path.append('./helper_functions')

songs = importlib.import_module('songs')
playlists = importlib.import_module('playlists')
artists = importlib.import_module('artists')

def app():
    print('Welcome to my CLI!')
    user_choice = 0
    while user_choice != 4:
        print(f'''
            Where would you like to go?
            1 - artists
            2 - songs
            3 - playlists
            4 - exit
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            return print('Thanks for using my CLI')
        else: 
            print("Invalid choice. Please try again.")

    
if __name__ == '__main__': 
    print("Welcome")
    app()
    print("Come Back Again!")