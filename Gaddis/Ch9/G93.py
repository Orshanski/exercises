CODE = {'А': ')', 'а': '0', 'Б': '(', 'б': '9', 'В': '*', 'в': '8',
        'Г': '&', 'г': '7', 'Д': '^', 'д': '6', 'Е': '%', 'е': '5',
        'Ж': '$', 'ж': '4', 'З': '#', 'з': '3', 'И': '@', 'и': '2',
        'Й': '!', 'й': '1', 'К': 'Z', 'к': 'z', 'Л': 'Y', 'л': 'y',
        'М': 'X', 'м': 'x', 'Н': 'W', 'н': 'w', 'О': 'V', 'о': 'v',
        'П': 'U', 'п': 'u', 'Р': 'T', 'р': 't', 'С': 'S', 'с': 's',
        'Т': 'R', 'т': 'r', 'У': 'Q', 'у': 'q', 'Ф': 'P', 'ф': 'p',
        'Х': 'O', 'х': 'o', 'Ц': 'N', 'ц': 'n', 'Ч': 'M', 'ч': 'm',
        'Ш': 'L', 'ш': 'l', 'Щ': 'K', 'щ': 'k', 'Ъ': 'я', 'ъ': 'Ы',
        'Э': 'А', 'э': 'а', 'Ю': 'з', 'ю': 'З', 'Я': 'о', 'я': 'о',
        '!': 'J', '@': 'I', 'ь': '|', '\n': '\n', ' ': ' ', 'ы': '/', '_': '_',
        '1': 'j', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g',
        '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd',
        '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a',
        ':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<',
        "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=',
        '{': '[', '[': '{', '}': ']', ']': '}'}

infile = open('../Data/wiedzmin', 'r', encoding='utf-8')
text = infile.read()

text_encoded = ''
for ch in text:
    ch = CODE[ch]
    text_encoded += ch

file_encoded = open('../Data/wiedzmin_encoded', 'w')
file_encoded.write(text_encoded)
file_encoded.close()

new_code = {}
for key, value in CODE.items():
    new_code[value] = key

file_encoded = open('../Data/wiedzmin_encoded', 'r')
text_encoded = file_encoded.read()

text_decoded = ''
for ch in text_encoded:
    ch = new_code[ch]
    text_decoded += ch

print(text_decoded)

