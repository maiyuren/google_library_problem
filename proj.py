
from libary_part2_processing import *

class Library:

    SCORES = None

    def __init__(self, lib_id):
        self.books = []
        self.sign_up_preocess = None
        self.max_ship_num = None
        self.num_books = None
        self.lib_id = lib_id

        # 0 for not-activated, -1 for activating, 1 for activated
        self.flag = 0

        # Sent books ids
        self.sent_books = []

    def remove_book(self, id):
        try:
            self.books.remove([id, Library.SCORES[id]])
            self.num_books -= 1
        except ValueError:
            pass

    def load_library(self, scores, info_line, book_line):

        self.num_books = info_line[0]
        self.sign_up_preocess = info_line[1]
        self.max_ship_num = info_line[2]

        for id in book_line:
            self.books.append([id, scores[id]])

        self.sort_books()

    def sort_books(self):
        self.books = sorted(self.books, key=lambda l: l[1])

    def get_books(self):
        """ This returns [id, value] for the best book """
        self.sent_books = self.sent_books + [i for i,_ in self.books[:self.max_ship_num]]
        return self.books[:self.max_ship_num]

    def get_value(self, days_left):
        effective_days = days_left - self.sign_up_preocess
        num_books = effective_days * self.max_ship_num
        if num_books > self.num_books:
            num_books = self.num_books

        return sum([i for _,i in self.books[:num_books]])

    def reduce_signup(self):
        self.sign_up_preocess -= 1
        if self.flag == 0:
            self.flag = -1
        if self.sign_up_preocess <= 0:
            self.flag = 1


def load_data(filename):

    """ Return info which is list of [num_books, num_libraries, num_days]"""

    libs = []

    with open(filename, 'r') as f:
        info = [int(i) for i in f.readline().split(' ')]
        scores = [int(i) for i in f.readline().split(' ')]

        for lib in range(info[1]):
            info_line = [int(i) for i in f.readline().split(' ')]
            book_line = [int(i) for i in f.readline().split(' ')]
            library = Library(lib)
            library.load_library(scores, info_line, book_line)
            libs.append(library)

    Library.SCORES = scores
    return info, libs


if __name__ == '__main__':

    filename = 'data_folder/d_tough_choices.txt'
    info, library_array = load_data(filename)
    days = info[2]

    MAX_VALUE, information = find_max_value(library_array, days)

    print(MAX_VALUE, information)

    with open('outputd.txt', 'w') as f:
        f.write(str(len(information))+'\n')

        for i,l_info in enumerate(information):
            f.write(' '.join(str(e) for e in l_info[0])+'\n')
            if i==len(information)-1:
                f.write(' '.join(str(e) for e in l_info[1]))
            else:
                f.write(' '.join(str(e) for e in l_info[1])+'\n')