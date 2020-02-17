infile = open('../Data/text', 'r')
text = infile.read()
infile.close()

count_upper_case = 0
count_lower_case = 0
count_digit = 0
count_spaces = 0

for ch in text:
    if ch.isupper():
        count_upper_case += 1
    if ch.islower():
        count_lower_case += 1
    if ch.isdigit():
        count_digit += 1
    if ch.isspace():
        count_spaces += 1

print(f'Количество букв в верхнем регистре - {count_upper_case}, в нижнем {count_lower_case}, цифр - {count_digit}, пробелов - {count_spaces}.')