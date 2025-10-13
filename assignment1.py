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
    print("Menu: ")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "D":
            print_books()
        user_input = input(">>> ")

def print_books():
    in_file = open("books.csv", "r")
    for line in in_file:
        print(line)
    in_file.close()


if __name__ == '__main__':
    main()
