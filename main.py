"""
This program returns seats in the theater, available for purchase.
Created by Grigorev Albert.
"""


def enter_seats(message):
    """ Checks if the seats are entered correctly. """
    while True:
        num_seats = input().split()
        try:
            num_seats = [int(item) for item in num_seats]
        except ValueError:
            print(message)
        else:
            break
    return num_seats


def number(message):
    """ Checks if the number is entered correctly. """
    while True:
        num = input(message)
        try:
            num = int(num)
        except ValueError:
            print('Enter number!')
        else:
            break
    return num


def can_buy(i_want, not_free, num_seats):
    """ Checks the possibility to buy a seats. """
    found = 0
    row = 0

    while found < i_want and row < num_seats[0]:
        found = 0
        row += 1
        for seat in range(1, num_seats[1]+1):
            found += 1
            if found == i_want:
                break
            if not_free.count([row, seat]):
                found = 0

    if found != 0:
        for seat_for_buy in range(seat-i_want+1, seat+1):
            print(row, seat_for_buy)
    else:
        print('There are no seats!')


def main():
    strings = ['Two numbers by space, please!',
               'One number, please!',
               'Enter number of rows and seats in it: ',
               'Enter number of not free seats: ',
               'How many seats do you want?']

    print(strings[2])
    num_seats = enter_seats(strings[0])

    num_not_free = number(strings[3])

    print('Enter not free seats:', end='\n')
    not_free = []
    for _ in range(num_not_free):
        not_free.append(enter_seats(strings[0]))

    i_want = number(strings[4])

    can_buy(i_want, not_free, num_seats)


if __name__ == '__main__':
    main()