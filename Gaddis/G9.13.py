infile = open('Data/pbnumbers', 'r')
pbnumbers = infile.read()
infile.close()

numbers = []
for number in pbnumbers.split():
    numbers.append(int(number))

numbers_count = {}
for number in numbers:
    numbers_count[number] = numbers.count(number)

numbers_count = list(numbers_count.items())
numbers_count.sort(key=lambda i: i[1])

for index in range(10):
    print((numbers_count[index])[0])

print('-------------------')

for index in range(len(numbers_count) - 1, len(numbers_count) - 10, -1):
    print((numbers_count[index])[0])