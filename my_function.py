def clear_text(text):
    """Очищает слова в тексте от знаков препинания и дефисов"""
    for index in range(len(text)):
        text[index] = text[index].lower()
        if text[index][-1] in ('.', '?', '!', '"', ',', ':'):
            ch = text[index][-1]
            text[index] = text[index].rstrip(ch)
        if text[index][0] == '"':
            text[index] = text[index].lstrip('"')

    while True:
        try:
            text.remove('-')
        except:
            break

    return text


def decline_the_word(word, count):
    if word == 'раз' and count in [2, 3, 4]:
        return 'раза'
    else:
        return 'раз'
