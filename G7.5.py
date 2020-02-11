infile = open('C:\\Users\\aorshanskiy\\OneDrive\\Books\\Гэддис. Начинаем программировать на Python\\data\\Исходный код\\Глава 07\\charge_accounts.txt', 'r')
accounts = infile.readlines()
infile.close()

index = 0
for element in accounts:
    accounts[index] = accounts[index].rstrip('\n')
    index += 1

test = input('Введите номер счета: ')
if test in accounts:
    print('Ура!')
else:
    print('Увы')