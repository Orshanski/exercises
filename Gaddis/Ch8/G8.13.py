def prepare_set(number_set):
    numbers = []
    for number in number_set:
        numbers.append(int(number))

    numbers_count = {}
    for number in numbers:
        numbers_count[number] = numbers.count(number)

    numbers_count = list(numbers_count.items())
    numbers_count.sort(key=lambda i: i[1])

    return numbers_count


def find_numbers(number_set, increase):
    numbers_count = prepare_set(number_set)

    if increase:
        for index in range(10):
            print((numbers_count[index])[0])
    else:
        for index in range(len(numbers_count) - 1, len(numbers_count) - 10, -1):
            print((numbers_count[index])[0])


infile = open('../Data/pbnumbers', 'r')
numbers_set = infile.read()
infile.close()

numbers_set = numbers_set.split()

find_numbers(numbers_set, True)
print('----------------------')
find_numbers(numbers_set, False)
print('----------------------')

pb_numbers = [numbers_set[i + 5:i + 6]
              for i in range(0, len(numbers_set), 6)]

game_numbers = [numbers_set[i:i + 5]
                for i in range(0, len(numbers_set), 6)]

pb_numbers_set = ''
for index in range(len(pb_numbers)):
    pb_numbers_set = pb_numbers_set + pb_numbers[index][0] + ' '

game_numbers_set = ''
for index in range(len(game_numbers)):
    for i in range(4):
        game_numbers_set = game_numbers_set + game_numbers[index][i] + ' '

pb_sorted = prepare_set(pb_numbers_set.split())
game_sorted = prepare_set(game_numbers_set.split())

pb_sorted.sort()
game_sorted.sort()

print('Частота каждого PowerBall числа:')
for element in pb_sorted:
    print(f'Число {element[0]} встречается {element[1]} раз')
print('---------------------------')

print('Частота чисел:')
for element in game_sorted:
    print(f'Число {element[0]} встречается {element[1]} раз')
