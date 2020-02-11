def print_invitation(guest_list):
    print('---------------------------')
    for name in guest_list:
        print(f'{name}, приглашаю Вас на праздник, посвященный чему-нибудь. В числе приглашенных:')
        for guest in guest_list:
            if guest == name:
                print('Вы')
            else:
                print(guest)
        print('---------------------------')


guest_list = ['Павел Бурыкин', 'Любовь Бурыкина', 'Вадим Зуев']
print_invitation(guest_list)
input('Нажмите для продолжения Enter')

guest_list[2] = 'Оршанская Софья'
print_invitation(guest_list)
input('Нажмите для продолжения Enter')

print('Список гостей был расширен')
guest_list.insert(0, 'Рябов Михаил')
guest_list.insert(2, 'Мирра Оршанская')
guest_list.append('Яков Оршанский')
print_invitation(guest_list)
input('Нажмите для продолжения Enter')

while len(guest_list) > 2:
    name = guest_list.pop()
    print(name + ', мне очень жаль, но приглашение на празднование чего-нибудь отменяется! Я сожалею!')

print_invitation(guest_list)
