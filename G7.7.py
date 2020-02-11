solution = ['A', 'C', 'A', 'A', 'D',
            'B', 'C', 'A', 'C', 'B',
            'A', 'D', 'C', 'A', 'D',
            'C', 'B', 'B', 'D', 'A']
infile = open('data/student_solution', 'r')
answers = infile.readlines()
infile.close()

index = 0
for answer in answers:
    answers[index] = answers[index].rstrip('\n')
    index += 1

correct_answers = 0
wrong_answers = []

index = 0
for answer in answers:
    if answers[index] == solution[index]:
        correct_answers += 1
    else:
        wrong_answers.append(index)
    index += 1

wrong_answers_string = ''
for answer in wrong_answers:
    wrong_answers_string += f'{answer + 1}, '

wrong_answers_string = wrong_answers_string.rstrip(', ')

print(f'Правильных ответов: {correct_answers}')
print(f'Неправильных ответов: {len(wrong_answers)}')
print (f'Номера неверных ответов: {wrong_answers_string}.')