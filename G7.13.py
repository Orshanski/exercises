import random

infile = open('data/Ball_responses', 'r', encoding='utf-8')
ball_responses = infile.readlines()
infile.close()

index = 0
for response in ball_responses:
    ball_responses[index] = ball_responses[index].rstrip('\n')
    index += 1

question = ''

while True:
    question = input("Введите вопрос или 'n', если не хотите продолжать: ")
    if question in ('n', 'N'):
        break
    print(ball_responses[random.randint(0, 11)])
