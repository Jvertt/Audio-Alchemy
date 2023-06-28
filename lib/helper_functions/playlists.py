def create():
    name = input("Enter the name: ")
    # Perform necessary operations to create a new playlist
    print(f"Created {name} successfully!")

def edit():
    id = input("Enter the ID of the playlist to edit: ")
    # Perform necessary operations to edit the playlist with the given ID
    print(f"Edited playlist with ID {id} successfully!")

def view():
    id = input("Enter the ID of the playlist to view: ")
    # Perform necessary operations to retrieve and display the playlist with the given ID
    print(f"Viewing playlist with ID {id}")

def delete():
    id = input("Enter the ID of the entity to delete: ")
    # Perform necessary operations to delete the playlist with the given ID
    print(f"Deleted playlist with ID {id} successfully!")

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