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
print('Расчет средней цены за год')
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
print()

# рассчитываем среднюю стоимость за месяц в каждом году
print('Расчет средней цены за месяц')
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
print()

# TODO Наибольшая и наименьшая цена в году

# TODO Список цен, упорядоченный по возрастанию