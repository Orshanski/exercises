infile = open('../Data/WorldSeriesWinners', 'r')
text = infile.readlines()

for index in range(len(text)):
    text[index] = text[index].rstrip('\n')

winners = {}
index = 0
for year in range(1903, 2009):
    if year not in [1904, 1994]:
        winners[year] = text[index]
        index += 1

winners_by_name = {}
for key, value in winners.items():
    try:
        winners_by_name[value] += 1
    except KeyError:
        winners_by_name[value] = 1

while True:
    year = input('Введите год с 1903 по 2008 или "n" для выхода: ')
    if year in ['n', 'N', 'н', 'Н']:
        print('Спасибо, до свидания!')
        break
    try:
        name = winners[int(year)]
        print(f'В {year} году выиграли {name}. Всего выигрышей в Мировой серии у команды: {winners_by_name[name]}.')
    except KeyError:
        if int(year) in [1904, 1994]:
            print(f'В {year} Мировая серия не проводилась.')
        else:
            print(f'За {year} год у нас данных нет.')
    except ValueError:
        print('Это не год!')
