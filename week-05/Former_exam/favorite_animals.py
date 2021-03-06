# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

from sys import argv

class Favourite:
    def __init__(self, file_name):
        self.file_name = file_name
        if len(argv) == 1:
            self.print_usage()
        elif len(argv) > 1:
            self.store_animal()

    def print_usage(self):
        print("favourite_animals.py 'animal' 'animal' .... ")

    def store_animal(self):
        for i in range(1, len(argv)):
            self.write_file(argv[i])

    def write_file(self, argument):
        with open(self.file_name, "r") as file_open:
            lines = file_open.readlines()
            file_open = open(self.file_name, "a")
            if argument + "\n" not in lines:
                file_open.write(argument + "\n")

favourite = Favourite("favourites.txt")