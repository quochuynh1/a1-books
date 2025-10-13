"""
CP1404 Assignment 1 - Books to Read
Name:
Date Started:
GitHub URL:
"""


def main():
    "Program to keep track of books to read"""
    print("Books to Read 1.0 by Quoc Huynh")
    pass

    in_file = open("books.csv", "r")

    print("Menu: ")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "D":
            print_books(in_file)
        elif user_input == "A":
            pass
        elif user_input == "C":
            pass
        else:
            print("Invalid menu choice")
        user_input = input(">>> ").upper()
    print("Quitting Program...")

    in_file.close()

def print_books(in_file):
    for line_number, line in enumerate(in_file):
        parts = line.strip().split(",")
        book_name = parts[0]
        author = parts[1]
        number_of_pages = parts[2]
        book_status = parts[3]
        if book_status == "u":
            print(f"*{line_number + 1}. {book_name} by {author} {number_of_pages}")
        else:
            print(f"{line_number + 1}. {book_name} by {author} {number_of_pages}")


if __name__ == '__main__':
    main()
