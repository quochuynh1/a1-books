"""
CP1404 Assignment 1 - Books to Read
Name:
Date Started:
GitHub URL:
"""

FILENAME = "books.csv"


def main():
    "Program to keep track of books to read"""

    print("Books to Read 1.0 by Quoc Huynh")
    pass

    print("Menu: ")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")
    user_input = input(">>> ").upper()
    print()
    while user_input != "Q":
        if user_input == "D":
            print_books(FILENAME)
        elif user_input == "A":
            pass
        elif user_input == "C":
            pass
        else:
            print("Invalid menu choice")
        user_input = input(">>> ").upper()
    print("Quitting Program...")


def print_books(filename):
    """"""
    total_unread_pages = 0
    total_unread_books = 0

    with open(filename, "r") as in_file:
        for line_number, line in enumerate(in_file):

            parts = line.strip().split(",")
            book_name = parts[0]
            author = parts[1]
            number_of_pages = int(parts[2])
            book_status = parts[3]

            if book_status == "u":
                print(f"*{line_number + 1:}. {book_name:<35} by {author:<15} {number_of_pages:} pages")
                # TODO: format output using max_length for spacing
                total_unread_pages += number_of_pages
                total_unread_books += 1
            else:
                print(f"{line_number + 1:>2}. {book_name:<35} by {author:<15} {number_of_pages:} pages")

    print(f"You still need to read {total_unread_pages} pages in {total_unread_books} books")


if __name__ == '__main__':
    main()
