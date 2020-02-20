
library_array = []

def remove_book_from_libraries(library_array,book_id):
    for libray in library_array:
        libray.remove_book(book_id)


def get_current_day_value(library_array):
    value = 0
    for library in library_array:
        if library.flag == 1:
            books_chosen = library.get_books()
            for book in books_chosen:
                book_id = book[0]
                book_value = book[1]
                value += book_value
                remove_book_from_libraries(library_array,book_id)
    return value


def get_next_library(library_array, days_left):
    # for each library find its value per day
    max_value = -1
    chosen_library = None
    for library in library_array:
        # can only check libraries which are not activated
        if library.flag == 0:
            value_per_day = library.get_value(days_left)
            # chooses the best library
            if value_per_day> max_value:
                max_value = value_per_day
                chosen_library = library

    return chosen_library


def find_max_value(library_array, days):
    MAX_VALUE = 0
    sign_up_lib = []
    for days_left in range(days, 0, -1):
        print("days left:", days_left)
        # find the value gained from today by scanning all libraries in running
        # pop out each book that has been scanned in activated and non activated
        MAX_VALUE += get_current_day_value(library_array)

        next_library_to_activate = None
        # if library is activating then that must be chosen
        for library in library_array:
            if library.flag == -1:
                next_library_to_activate = library

        if not next_library_to_activate:
            next_library_to_activate = get_next_library(library_array, days_left)
            if next_library_to_activate:
                sign_up_lib.append(next_library_to_activate.lib_id)
        if next_library_to_activate:
            next_library_to_activate.reduce_signup()

    information = []
    for id in sign_up_lib:
        info = (id, len(library_array[id].sent_books))
        information.append([info, library_array[id].sent_books])

    return MAX_VALUE,  information



