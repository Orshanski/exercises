my_string = input('Введите 20 чисел через пробел:').split()
print(my_string)
my_digits =[]

for element in my_string:
    try:
       my_digits.append(float(element))
    except:
        print(f'{element} не число!')

min_index = my_digits.index(min(my_digits))
max_index = my_digits.index(max(my_digits))

print(f'Сумма чисел в списке {sum(my_digits)}')
print(f'Среднее арифметическое значение чисел в списке {sum(my_digits)/12:.2f}')
print(f'Наименьшее число {min(my_digits)}')
print(f'Наибольшее число {max(my_digits)}')
