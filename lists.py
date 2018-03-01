"""Lists exercises from the book Python Crash Course"""

def pizzas():
    """stores pizza toppings in a lists and loops over them"""

    toppings = ["pepperoni", "bbq", "hawaiian", "pesto"]

    for topping in toppings:
        print topping

    print "I F@#$!ing love pizza!!"


def count_to_x(x):
    """creates a list from 1 through x, stores in a list"""

    number_list = []

    for count in range(1, x+1):
        
        number_list.append(count)
        print count


def one_million():
    """creates a list from 1 to 1 million"""

    million = []

    for count in range(1, 1000001):
        million.append(count)

    print min(million)
    print max(million)

    return million

def print_odd():
    """prints odd numbers from 1 to 20"""

    one_to_twenty = []

    for count in range(1, 21):
        one_to_twenty.append(count)

    print one_to_twenty

    for i in range(1, (len(one_to_twenty)+1), 2):
        print i




