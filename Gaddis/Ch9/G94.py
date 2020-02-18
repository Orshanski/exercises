import my_function as mf

infile = open('../Data/wiedzmin', 'r', encoding='utf-8')
text = infile.read()

text = text.split()
text = mf.clear_text(text)

unique_words = set(text)
print(sorted(unique_words))