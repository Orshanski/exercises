import my_function as mf

infile = open('../Data/wiedzmin', 'r', encoding='utf-8')
text = infile.read()

text_set = set(mf.clear_text(text.split()))

text = text.splitlines()
str_text = []

for string in text:
    tmp = mf.clear_text(string.split())
    str_text.append(tmp)

text_index = {}

''' вариант со сборкой строки в качестве значения:
for word in text_set:
    for string in str_text:
        if word in string:
            try:
                text_index[word] = text_index[word] + ', ' + str(str_text.index(string))
            except KeyError:
                text_index[word] = str(str_text.index(string))'''

# более экономный вариант со списком в качестве значения
for word in text_set:
    for string in str_text:
        if word in string:
            try:
                text_index[word].append(str(str_text.index(string)))
            except KeyError:
                text_index[word] = [str(str_text.index(string))]

list_text_index = list(text_index.items())
list_text_index.sort()


index_file = open('../Data/wiedzmin_index', 'w', encoding='utf8')
new_string = ''
for element in list_text_index:
    new_string = f'Слово "{element[0]}" встречается в строках номер: {", ".join(element[1])} \n'
    index_file.writelines(new_string)
