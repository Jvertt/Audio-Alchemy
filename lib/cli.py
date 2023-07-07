import sys
import importlib
sys.path.append('./helper_functions')
import pyfiglet

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# Generate ASCII art banner using Pyfiglet
def print_banner(text, color=Color.GREEN, font="big"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    colored_ascii_art = color + ascii_art + Color.RESET
    print(colored_ascii_art)

songs = importlib.import_module('songs')
playlists = importlib.import_module('playlists')
artists = importlib.import_module('artists')

def app():
    user_choice = 0
    while user_choice != 4:
        print(f'''

            Where would you like to go?
            ---------------------------
            1 - {Color.GREEN}artists{Color.RESET}

            2 - {Color.GREEN}songs{Color.RESET}

            3 - {Color.GREEN}playlists{Color.RESET}

            4 - {Color.RED}exit{Color.RESET}
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            artists.module()
        elif user_choice == 2:
            songs.module()
        elif user_choice == 3:
            playlists.module()
        elif user_choice == 4:
            return print_banner("Come Back Again !")
        else: 
            print("Invalid choice. Please try again.")

    
if __name__ == '__main__': 
    print_banner("Audio Alchemy", color=Color.GREEN)
    app()
