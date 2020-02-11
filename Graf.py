import matplotlib.pyplot as plt


def plt_graf():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords, )
    plt.title('Продажи с разбивкой по годам')

    plt.xlabel('Год')
    plt.ylabel('Объем продаж')

    # организуем подписи данных
    plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$lm', '$2m', '$3m', '$4m', '$5m'])

    plt.grid(True)

    plt.show()

def plt_bar():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]

    bar_width = 5
    # строим диаграмму и определяем цвета
    plt.bar(left_edges, heights, bar_width, color = ('r', 'g', 'b'))

    plt.show()

plt_graf()
plt_bar()
