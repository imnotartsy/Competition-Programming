# import enchant
import nltk
from nltk.corpus import words
nltk.download('words')
# >>> d = enchant.Dict("en_US")
# >>> d.check("Hello")

letters = ["A", "T", "U", "D", "I"]

for i in range(len(letters)):
    for j in range(len(letters)):
        for k in range(len(letters)):
            for l in range(len(letters)):
                for m in range(len(letters)):

                    if len(set([i, j, k, l, m])) == 5:
                        word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] 
                        print(word)
                        if word in words.words():
                            print("***FOUND***")

print(len(words.words()))
# print("hullo")