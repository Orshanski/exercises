def count_consonants(sentence):
    cons_count = 0
    for ch in sentence:
        if ch.lower() in consonants:
            cons_count += 1
    return cons_count


def count_vowels(sentence):
    vow_count = 0
    for ch in sentence:
        if ch.lower() in vowels:
            vow_count += 1
    return vow_count


consonants = ['б', 'в', 'г', 'д', 'е', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
              'щ', 'ъ', 'ь']
vowels = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']

sentence = input('Введите предложение: ')

consonants_count = count_consonants(sentence)
vowels_count = count_vowels(sentence)

print(f'Гласных букв - {vowels_count}, согласных букв - {consonants_count}.')