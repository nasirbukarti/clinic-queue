# city hospital system
queue = []
total_seen = 0

def show_menu():
    print("\n--- City Hospital Patient Portal ---")
    print("1. Register Patient (Add to Queue)")
    print("2. View Waiting List")
    print("3. See Next Patient (Remove from Queue)")
    print("4. view Daily Tally")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Select an option (1-5): ")

    if choice == '1':
        name = input("Amina Sani Shuibu: ")
        print("Processing registration...")
        queue.append(name) # Adds to the end (FIFO)
        print(f"Patient {name} registered.")

    elif choice == '2':
        if not queue:
            print("The waiting list is empty.")
        else:
            print("\nCurrent Waiting List:")
            for i, patient in enumerate(queue, 1):
                print(f"{i}. {patient}")

    elif choice == '3':
        if not queue:
            print("No patients in the queue.")
        else:
            removed = queue.pop(0) # Removes the FIRST person (FIFO)
            total_seen += 1
            print(f"Now seeing: {removed}")

    elif choice == '4':
        print(f"Total patients seen today: {total_seen}")

    elif choice == '5':
        print("Closing Clinic Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        