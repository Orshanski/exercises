def simple(number):
    if simple_number[number] == True:
        return True
    else:
        return False

n = input('Введите число: ')
n = int(n)

simple_number = {0:False}

for index in range(n):
    simple_number[index + 1] = True

i = 2

while (i ** 2) < n:
    k = 2
    while  i * k <= n:
        simple_number[i * k] = False
        k += 1
    i += 1

my_simple_number = []

for index in range(n + 1):
    if simple(index) == True:
        my_simple_number.append(index)

print(my_simple_number)