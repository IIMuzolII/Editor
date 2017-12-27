import random

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

word = input("Type the word here: ")
len_word = len(word)
anagrama = ''
word_fact = fatorial(len_word)

for i in range(word_fact):
    raffle = random.sample(range(len_word), len(word))

    for i in raffle:
        temp_int = int(i)
        temp_word = word[temp_int]
        anagrama += temp_word

    if len(anagrama) == len_word:
        print(anagrama)
        with open('Anagrama.txt', 'a') as fl:
            fl.write(anagrama+'\n')
        anagrama = ''
