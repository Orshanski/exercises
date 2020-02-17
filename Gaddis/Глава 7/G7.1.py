days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

income = []
for day in days_of_week:
    inc_is_digit = False
    prompt = f"В {day} продажи составили, руб: "
    while not inc_is_digit:
        try:
            income.append(float(input(prompt)))
            inc_is_digit = True
        except:
            print('Введите число!')

print('------------------------------------------------')
print(f'За неделю выручка составила {sum(income):.2f} рублей.')