from itertools import permutations

words = permutations('ATTESTAT')
set_words = set()
for w in words:
    word = ''.join(w)
    t = word.replace('E', 'A').replace('S', 'T')
    if 'AA' in t or 'TT' in t:
        set_words.add(word)
print(len(set_words))