def write_student_data():
    with open('student_data.txt', 'w') as file:
        while True:
            key = input("Enter attribute (or 'done' to finish): ")
            if key.lower() == 'done':
                break
            value = input(f"Enter {key}: ")
            file.write(f"{key}: {value}\n")
    print("Data successfully written to student_data.txt")

def read_student_data():
    try:
        with open('student_data.txt', 'r') as file:
            print("\n--- Student Data ---")
            print(file.read())
    except FileNotFoundError:
        print("Error: File 'student_data.txt' not found.")

def append_student_data():
    try:
        with open('student_data.txt', 'a') as file:
            file.write("Email: abc@gmail.com\n")
            file.write("Roll: 2014/25\n")
        print("Additional data appended successfully.")
    except FileNotFoundError:
        print("Error: Cannot append. File not found.")

def count_words():
    try:
        with open('student_data.txt', 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found.")

def main_menu():
    while True:
        print("\n--- Student Data File Operations ---")
        print("1. Write Student Data")
        print("2. Read Student Data")
        print("3. Append Student Data")
        print("4. Count Words")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            write_student_data()
        elif choice == '2':
            read_student_data()
        elif choice == '3':
            append_student_data()
        elif choice == '4':
            count_words()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
