infile = open('Data/USPopulation', 'r')
population_str = infile.readlines()
infile.close()

population = []

for number in population_str:
    population.append(int(number.rstrip('\n')))

population_change = []

index = 0
year = 1951
while index < 40:
    population_change.append([year, population[index + 1] - population[index]])
    index += 1
    year +=1

# Находим минимальный прирост населения, используя упаковку и list
min_growth = min(list(zip(*population_change))[1])
index = list(zip(*population_change))[1].index(min(list(zip(*population_change))[1]))
min_growth_year = list(zip(*population_change))[0][index]

# Находим максимальный прирост населения, используя упаковку и list
max_growth = min(list(zip(*population_change))[1])
index = list(zip(*population_change))[1].index(min(list(zip(*population_change))[1]))
max_growth_year = list(zip(*population_change))[0][index]

# Находим средний прирост населения, используя упаковку и list
avg = sum(list(zip(*population_change))[1])/len(population_change)

print(f'Среднегодовое изменение численности населения: {avg:,.2f} млн. чел.')
print(f'Наименьший прирост населения был {min_growth} млн. чел. в {min_growth_year} году.')
print(f'Наибольший прирост населения был {max_growth} млн. чел. {max_growth_year} году.')