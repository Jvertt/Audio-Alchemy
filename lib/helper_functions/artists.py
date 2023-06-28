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
            1 - Create artist
            2 - Edit artist
            3 - View artists
            4 - Delete artist
            5 - back
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