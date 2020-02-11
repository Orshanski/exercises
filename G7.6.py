def compare (list, digit):
    print(f'Эти числа больше {digit}:')
    for element in list:
        if element > digit:
            print(element)

my_list = [3, 5, 4, 34, 28, 456]
my_digit = 20

compare(my_list, my_digit)