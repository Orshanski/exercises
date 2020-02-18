import my_function as mf

infile = open('../Data/wiedzmin', 'r', encoding='utf-8')
text = infile.read()

text = text.split()
text = mf.clear_text(text)

count_word = {}
for word in text:
    try:
        count_word[word] += 1
    except KeyError:
        count_word[word] = 1

list_count_word = list(count_word.items())
list_count_word.sort(key=lambda i: i[1], reverse=True)

for element in list_count_word:
    print(f'Слово "{element[0]}" встречается в тексте {element[1]} {mf.decline_the_word("раз", element[1])}')