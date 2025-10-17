"""
CP1404 Assignment 1 - Books to Read
Name: Quoc Huynh
Date Started: 13/10/25
GitHub URL: https://github.com/cp1404-students/a1-books-quochuynh1
"""

FILENAME = "test_books.csv"


def main():
    "Program to keep track of books to read"""

    book_data = load_books(FILENAME)

    print("Books to Read 1.0 by Quoc Huynh")
    print(f"{len(book_data)} books loaded.")

    print("Menu: ")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")
    user_input = input(">>> ").upper()

    while user_input != "Q":
        if user_input == "D":
            book_data = load_books(FILENAME)
            print_books(book_data)
        elif user_input == "A":
            add_books(FILENAME)
        elif user_input == "C":
            book_data = load_books(FILENAME)
            complete_books(FILENAME, book_data)
        else:
            print("Invalid menu choice")
        print("Menu: ")
        print("D - Display books")
        print("A - Add a new book")
        print("C - Complete a book")
        print("Q - Quit")
        user_input = input(">>> ").upper()
    pass  # save the books file once
    print("Quitting Program...")


def load_books(filename):
    """Load book information as a list of lists for other functions to access"""
    with open(FILENAME, "r") as in_file:
        book_data = [line.strip().split(",") for line in in_file]
        return book_data


def print_books(book_data):
    """Print the book data as well as how many pages and books are still left to be read"""
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
            print(
                f"*{line_number + 1:}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")
            total_unread_pages += number_of_pages
            total_unread_books += 1
        else:
            print(f"{line_number + 1:>2}. {book_name:{max_name_length}} by {author:{max_author_length}} {number_of_pages:{max_page_length}} pages")

    if total_unread_books == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {total_unread_pages} pages in {total_unread_books} books")


def add_books(filename):
    """Add new book data on top of existing book data with input validation"""
    title = input("Title: ").strip()
    while title == "":
        print("Input can not be blank")
        title = input("Title: ").strip()

    author = input("Author: ").title().strip()
    while author == "":
        print("Input can not be blank")
        author = input("Author: ").title().strip()

    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_pages = int(input("Number of Pages: "))
            if number_of_pages <= 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
                print(f"{title} by {author} ({number_of_pages} pages) added.")
        except ValueError:
            print("Invalid input - please enter a valid number")

    new_book_data = f"{title},{author},{number_of_pages},{"u"}\n"

    with open(filename, "r") as in_file:
        existing_data = in_file.read()

    with open(filename, "w") as out_file:
        out_file.write(new_book_data + existing_data)

    return out_file


def complete_books(filename, book_data):
    """Change status of book to completed with input validation"""
    if all(book[3] == "c" for book in book_data):
        print("No unread books - well done!")
        return
    else:
        print_books(book_data)
        print("Enter the number of a book to make as completed")

    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(">>> "))
            if number <= 0:
                print("Number must be > 0")
            else:
                book_record = book_data[number - 1]
                book_to_complete = book_record[0]
                author = book_record[1]
                book_status = book_record[3]

                if book_status == "c":
                    print("That book is already completed")
                else:
                    book_record[3] = "c"
                    print(f"{book_to_complete} by {author} Completed!")

                with open(filename, "w") as out_file:
                    for record in book_data:
                        out_file.write(",".join(record) + "\n")

                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")
        except IndexError:
            print("Invalid book number")


if __name__ == '__main__':
    main()
