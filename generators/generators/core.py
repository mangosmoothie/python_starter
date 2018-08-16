from .date_generator import generate_date
from .number_generator import generate_numbers


def get_date():
    return generate_date()


def get_numbers():
    return generate_numbers()


# print output of get_date if calling "as a script"
if __name__ == '__main__':
    print(get_date())
