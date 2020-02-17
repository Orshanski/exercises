def clear_text(text):
    """Очищает слова в тексте от знаков препинания и дефисов"""
    for index in range(len(text)):
        text[index] = text[index].lower()
        if text[index][-1] in ('.', '?', '!', '"', ','):
            ch = text[index][-1]
            text[index] = text[index].rstrip(ch)
        if text[index][0] == '"':
            text[index] = text[index].rstrip('"')

    while True:
        try:
            text.remove('-')
        except:
            break

    return text
