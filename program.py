# 8 May 2018
""" This program will ask a user for the birthday then compute the number of days until the user's next birthday."""
import datetime


def print_header():
    print('--------------------------')
    print('      BIRTHDAY APP')
    print('--------------------------')


def get_birthday():
    print('What day were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_till_birthday(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print('You had your birhtday {} days ago this year!'.format(abs(days)))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Happy birthday!!!')


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_till_birthday(bday, today)
    print_birthday_info(number_of_days)


main()
