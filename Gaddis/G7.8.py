infile = open('Data/BoyNames', 'r')
boy_names = infile.readlines()
infile.close()

index = 0
for name in boy_names:
    boy_names[index] = boy_names[index].rstrip('\n')
    index += 1

infile = open(
    'Data/GirlNames', 'r')

girl_names = infile.readlines()
infile.close()

index = 0
for name in girl_names:
    girl_names[index] = girl_names[index].rstrip('\n')
    index += 1

girl_name = input("Введите имя девочки или 'n', если не хотите: ")
boy_name = input("Введите имя мальчика или 'n', если не хотите: ")

if not girl_name == 'n':
    if girl_name in girl_names:
        print('Имя девочки - в списке популярных!')
    else:
        print('Такого имени в списке популярных девичьих имен нет!')

if not boy_name == 'n':
    if boy_name in boy_names:
        print('Имя мальчика - в списке популярных!')
    else:
        print('Такого имени в списке популярных имен мальчиков нет!!')