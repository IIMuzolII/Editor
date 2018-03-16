#The anagramx file generate all the possibility of a word be mixed
#Last Update: 12/29/2017

import random

def factorial(x):
    """
        Generete the Factorial of the number passed.
    """
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

try:
    word = input("Type the word here: ")
except:
    print("ERROR INVALID INPUT")
    
len_word = len(word)
anagrama = ''
word_fact = factorial(len_word)

for i in range(word_fact):
    raffle = random.sample(range(len_word), len_word)

    for i in raffle:
        temp_int = int(i)
        temp_letter = word[temp_int]
        anagrama += temp_letter

    if len(anagrama) == len_word:
        print(anagrama)
        with open('Anagram.txt', 'a') as fl:
            fl.write(anagrama+'\n')# Open a file 'Anagram' and write the word in it
        anagrama = ''
