import nltk
import itertools

nltk.download('words')
word_list = set(nltk.corpus.words.words())

query = input('Enter search query: ')

res = []

permutations = itertools.permutations(query)
for permutation in permutations:
    res.append(''.join(permutation))

for entry in set(res):
    if entry in word_list:
        print(entry)
