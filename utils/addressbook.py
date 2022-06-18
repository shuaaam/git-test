from collections import UserDict
import shelve

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

        filename = 'database/ab_data'
        dt = self.data

        with shelve.open(filename) as fn:
                fn['dt'] = dt

        with shelve.open(filename) as states:
            for key in states:
                print('file loaded')