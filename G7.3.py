# Количество осадков по месяцам
# [39.0, 33.9, 39.5, 43.1, 63.4, 62.9, 77.5, 45.8, 54.5, 44.8, 40.2, 45.8]
rain = []

names_of_the_month = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']

for month in names_of_the_month:
    inc_is_digit = False
    prompt = f"В {month} выпало осадков, в мм.: "
    while not inc_is_digit:
        try:
            rain.append(float(input(prompt)))
            inc_is_digit = True
        except:
            print('Введите число!')

min_index = rain.index(min(rain))
max_index = rain.index(max(rain))

print(f'Суммарное количество осадков за год составило {sum(rain)} мм.')
print(f'Среднее количество осадков в месяц составило {sum(rain)/12:.2f} мм.')
print(f'Наименьшее количество осадков было в {names_of_the_month[min_index]}.')
print(f'Наибольшее количество осадков было в {names_of_the_month[max_index]}.')

