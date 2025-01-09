def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter shopping item: ")
            shopping_list.add(add_item)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter removing Item: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print("Item Not Found!")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()