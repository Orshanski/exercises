infile = open('Data/charge_accounts', 'r')
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