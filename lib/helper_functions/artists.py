def create():
    name = input("Enter the artist's name: ")
    print(f"Artist '{name}' created successfully!")

def edit():
    artist_id = input("Enter the ID of the artist to edit: ")
    # Logic to edit the artist with the given ID
    print(f"Artist with ID '{artist_id}' edited successfully!")

def view():
    print("Listing all artists:")

def delete():
    artist_id = input("Enter the ID of the artist to delete: ")
    # Logic to delete the artist with the given ID
    print(f"Artist with ID '{artist_id}' deleted successfully!")

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