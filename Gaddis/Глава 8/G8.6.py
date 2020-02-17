infile = open('../Data/text', 'r')
text = infile.readlines()
infile.close()

words = []

for sentence in text:
    words.append(len(sentence.split()))

average = sum(words)/len(words)
print(average)