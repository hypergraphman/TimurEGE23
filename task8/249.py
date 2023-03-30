from itertools import product

words = product('АПРСУ', repeat=5)
k = 1
for w in words:
    word = ''.join(w)
    if word[0] == 'У' and word.count('А') == 2 and 'АА' not in word:
        print(k, word)
    k += 1