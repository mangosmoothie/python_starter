import sys
from generators import get_date, get_numbers

options = """
Please select an option:

1 - get current date
2 - get a list of numbers
3 - exit program
"""


if __name__ == '__main__':
    option = ""
    while(option != "3"):
        option = input(options)
        if option == "1":
            print(get_date())
        elif option == "2":
            print(get_numbers())
        elif option == "3":
            sys.exit()
