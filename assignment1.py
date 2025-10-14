"""
CP1404 Assignment 1 - Books to Read
Name:
Date Started:
GitHub URL:
"""

FILENAME = "books.csv"


def main():
    "Program to keep track of books to read"""

    with open(FILENAME, "r") as in_file:

        book_data = [line.strip().split(",") for line in in_file]

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
                print_books(in_file, book_data)
            elif user_input == "A":
                pass
            elif user_input == "C":
                pass
            else:
                print("Invalid menu choice")
            user_input = input(">>> ").upper()
        pass # save the books file once
        print("Quitting Program...")


def print_books(in_file, book_data):
    """"""
    total_unread_pages = 0
    total_unread_books = 0

    max_name_length = max(len(book[0]) for book in book_data)
    max_author_length = max(len(author[1]) for author in book_data)
    max_page_length = max(len(author[2]) for author in book_data)

    for line_number, part in enumerate(book_data):

        book_name = part[0]
        author = part[1]
        number_of_pages = int(part[2])
        book_status = part[3]

        if book_status == "u":
            print(f"*{line_number + 1:}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")
            total_unread_pages += number_of_pages
            total_unread_books += 1
        else:
            print(f"{line_number + 1:>2}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")

    print(f"You still need to read {total_unread_pages} pages in {total_unread_books} books")


if __name__ == '__main__':
    main()
