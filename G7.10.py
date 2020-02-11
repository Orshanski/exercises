infile = open('data/WorldSeriesWinners', 'r')
ws_winners = infile.readlines()
infile.close()

index = 0
for winner in ws_winners:
    ws_winners[index] = ws_winners[index].rstrip('\n')
    index += 1

team = input('Введите название команды: ')

wins = ws_winners.count(team)

if wins == 0:
    print('Такая команда не выигрывала Мировую серию по бейсболу')
else:
    print(f'{wins} раз команда выигрывала Мировую серию по бейсболу')
