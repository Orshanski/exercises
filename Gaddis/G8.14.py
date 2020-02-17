# 02-11-2013:3.677
def number_to_month(number):
    if number == 1: return 'январе'
    elif number == 2: return 'феврале'
    elif number == 3: return 'марте'
    elif number == 4: return 'апреле'
    elif number == 5: return 'мае'
    elif number == 6: return 'июне'
    elif number == 7: return 'июле'
    elif number == 8: return 'августе'
    elif number == 9: return 'сентябре'
    elif number == 10: return 'октябре'
    elif number == 11: return 'ноябре'
    elif number == 12: return 'декабре'


infile = open('Data/GasPrice', 'r')
prices = infile.read()
infile.close()

prices = prices.split()

prices_list = []
index = 0
for element in prices:
    month = int(element[0:2])
    day = int(element[3:5])
    year = int(element[6:10])
    price = float(element[11:len(element)])
    prices_list.append([day, month, year, price])

# рассчитываем среднюю цену за год
print('--------------------------------------------------------------------------------------------------------------')
print('Расчет средней цены за год')
print()
average_prices_in_year = []
for year in range(1993, 2014):
    price_sum = 0
    count = 0
    for element in prices_list:
        if element[2] == year:
            price_sum += element[3]
            count += 1
    average_price = price_sum / count
    average_prices_in_year.append([year, average_price])

for element in average_prices_in_year:
    print(f'Средняя цена в {element[0]} составила ${element[1]:.2f}')
print('---------------------------------------------------------------------------------------------------------------')

# рассчитываем среднюю стоимость за месяц в каждом году
print('Расчет средней цены за месяц')
print()
average_prices_in_month = []
for year in range(1993, 2014):
    for month in range(1, 13):
        price_sum = 0
        count = 0
        for element in prices_list:
            if element[2] == year and element[1] == month:
                price_sum += element[3]
                count += 1
        try:
            average_price = price_sum / count
            average_prices_in_month.append([year, month, average_price])
        except:
            average_prices_in_month.append([year, month, 'Нет данных'])

for element in average_prices_in_month:
    if not element[2] == 'Нет данных':
        print(f'В {number_to_month(element[1])} {element[0]} года средняя стоимость топлива составила ${element[2]:.2f}')
print('---------------------------------------------------------------------------------------------------------------')

# Находим наибольшую и наименьшую цену в году
print('Расчет наименьшей и наибольшей цены в году')
print()
min_price_in_year = {}
max_price_in_year = {}

# Заполняем словари первичными значениями, взяв за минимальную и максимальную цену первую цену в году.
# Второе значение - индекс минимальной цены в году в общем листе цен.
for year in range(1993, 2014):
    for index in range(len(prices_list)):
        if prices_list[index][2] == year:
            min_price_in_year[year] = [prices_list[index][3], index]
            max_price_in_year[year] = [prices_list[index][3], index]
            break


for year in range(1993, 2014):
    min_price = min_price_in_year[year][0]
    min_index = min_price_in_year[year][1]
    max_price = max_price_in_year[year][0]
    max_index = max_price_in_year[year][1]
    for index in range(len(prices_list)):
        if prices_list[index][2] == year:
            if min_price > prices_list[index][3]:
                min_price = prices_list[index][3]
                min_index = index
            if max_price < prices_list[index][3]:
                max_price = prices_list[index][3]
                max_index = index
    min_price_in_year[year] = prices_list[min_index]
    max_price_in_year[year] = prices_list[max_index]

for year in range(1993, 2014):
    print(f'В {min_price_in_year[year][2]} минимальная цена топлива была ${min_price_in_year[year][3]:.2f}, а '
          f'максимальная - ${max_price_in_year[year][3]:.2f}')

# Формируем файл со списком цен, упорядоченный по возрастанию
new_price_list = []

while not len(prices_list) == 0:
    min_price = prices_list[0][3]
    min_index = 0
    for index in range(len(prices_list)):
        if min_price > prices_list[index][3]:
            min_price = prices_list[index][3]
            min_index = index
    new_price_list.append(prices_list.pop(min_index))

low_to_high = open('Data/low_to_high', 'w')
high_to_low = open('Data/high_to_low', 'w')
new_string = ''
for element in new_price_list:
    if len(str(element[0])) > 1:
        day = str(element[0])
    else:
        day = '0' + str(element[0])
    if len(str(element[1])) > 1:
        month = str(element[1])
    else:
        month = '0' + str(element[1])
    new_string = day + '-' + month + '-' + str(element[2]) + ':' + f'{element[3]:.3f}' + '\n'
    low_to_high.writelines(new_string)

new_string = ''
for index in range(len(new_price_list)-1, -1, -1):
    element = new_price_list[index]
    if len(str(element[0])) > 1:
        day = str(element[0])
    else:
        day = '0' + str(element[0])
    if len(str(element[1])) > 1:
        month = str(element[1])
    else:
        month = '0' + str(element[1])
    new_string = day + '-' + month + '-' + str(element[2]) + ':' + f'{element[3]:.3f}' + '\n'
    high_to_low.writelines(new_string)