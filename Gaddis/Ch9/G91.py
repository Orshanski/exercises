courses = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']
courses_classrooms = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}
courses_teachers = {
    'CS101': 'Хайнс',
    'CS102': 'Альвардо',
    'CS103': 'Рич',
    'NT110': 'Берк',
    'CM241': 'Ли'
}
courses_time = {
    'CS101': '08:00',
    'CS102': '09:00',
    'CS103': '10:00',
    'NT110': '11:00',
    'CM241': '13:00'
}

while True:
    course = input('Введите номер курса: ')
    if course in ('n', 'N'):
        break
    if course not in courses:
        print('Недопустимый номер курса')
    else:
        print(f'Данные по курсу {course}:')
        print(f'Аудитория: {courses_classrooms[course]}')
        print(f'Преподаватель: {courses_teachers[course]}')
        print(f'Время начала: {courses_time[course]}')
