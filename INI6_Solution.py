#opening file for reading
file = open("C:\\Users\\benko\\Downloads\\rosalind_ini6 (1).txt", "r")
#establish our dictionay
dict = {}
#split the text into words
text = file.read()
words = text.split()
word_counts = {}
#process words and add to dictionary
for word in words:
    if word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
for word, count in word_counts.items():
    print(f'{word} {count}')