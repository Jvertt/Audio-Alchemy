def create():
    pass

def edit():
    pass

def view():
    pass

def delete():
    pass

def module():
    user_choice = 0
    while user_choice != 5:
        print('''
         Where would you like to go?
            1 - Create playlist
            2 - Edit playlist
            3 - View playlists
            4 - Delete playlist
            5 - Back
        ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice == 1:
            create()
        elif user_choice == 2:
            edit()
        elif user_choice == 3:
            view()
        elif user_choice == 4:
            delete()
        elif user_choice == 5:
            print('Going back to the main menu.')
        else:
            print("Invalid choice. Please try again.")