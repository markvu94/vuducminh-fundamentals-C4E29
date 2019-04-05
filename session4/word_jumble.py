word = "champion"
wordlist = list(word)
shuffle = []
from random import choice
for i in range (len(wordlist)):
    character = choice(wordlist)
    shuffle.append(character)
    wordlist.remove(character)
print(*shuffle, sep = "")

