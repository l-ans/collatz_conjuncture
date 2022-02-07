

# A method which returns the collatz tuple of a given integer with all the numbers
def collatz_generation(number):
    collatz_tuple = [number]
    i = 0
    while True:
        if number == 1:
            return collatz_tuple
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        collatz_tuple.append(number)
        i += 1
        if number == 1:
            return collatz_tuple


# method that returns the length of a collatz tupel
def tuple_length(int_number):
    collatz_tuple = collatz_generation(int_number)
    return len(collatz_tuple)


# method which returns the highest reached number of a given integer
def tuple_height(int_number):
    collatz_tuple = collatz_generation(int_number)
    collatz_tuple.sort()
    return collatz_tuple[-1]


# method which compares the initial value to the max value to look if max(a1) > a1
def height_generation(calc_amount):
    y = 1
    for x in range(calc_amount):
        var = collatz_generation(y)
        if var[0] >= tuple_height(y):
            print("Starting number: " + str(var[0]) + " max:" + str(tuple_height(y)))

        y += 1


# method which returns the tuple as: [initial value, length, max]
def storage_efficient_tuple(int_number):
    e_tuple = [int_number, tuple_length(int_number), tuple_height(int_number)]
    return e_tuple


# method which finds the height-champions in a given range
def h_champions(calc_amount):
    champions = []
    x = 1
    old_champion = 0
    for i in range(calc_amount):
        number = tuple_height(x)
        if old_champion < number:
            champions.append([x, number])
            old_champion = number
        x += 1
    return champions


# method which finds the length-champions in a given range
def l_champions(calc_amount):
    champions = []
    x = 1
    old_champion = 0

    for i in range(calc_amount):
        number = tuple_length(x)

        if old_champion < number:
            champions.append([x, number])
            old_champion = number
        x += 1
    return champions


# method which finds the relation between two tupel
def relation(number1, number2):
    c1 = collatz_generation(number1)
    c2 = collatz_generation(number2)
    if len(c1) < len(c2):
        if c1[0] == c2[-len(c1)]:
            return "The tupel " + str(number1) + " and " + str(number2) + " are related by " + str(len(c2) - len(c1))
    elif len(c2) < len(c1):
        if c2[0] == c1[-len(c2)]:
            return "The tupel " + str(number1) + " and " + str(number2) + " are related by " + str(len(c1) - len(c2))
    return "The tupel " + str(number1) + " and " + str(number2) + " aren't related"
