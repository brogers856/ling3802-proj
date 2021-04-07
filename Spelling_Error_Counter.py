# File: Spelling_Error_Counter.py

import string
from spellchecker import SpellChecker

#Used for the spell checker
spell = SpellChecker()

#Number of incorrect spellings
count = 0

#Total number of words
total_count = 0


#Sample Text
txt = "The terrifick beegle jumped throo the hoopz."


#Gets rid of all punctuation
#Can't detect numbers and will assume it is correct
#Only detects if a word is not in the english dictionary, not if it it's grammatically correct
# If there is not a space between punctuation such as lazy dog!I hate him ...... then it will go to lazy dogI hate him something to think about
string_without_punctuation = txt.translate(str.maketrans('','',string.punctuation))

#Creates an array of all the words in the sentence
split_txt = string_without_punctuation.split()


print(split_txt)

total_count = len(split_txt)


# Find those words that may be misspelled
misspelled = spell.unknown(split_txt)

for word in misspelled:
    count = count + 1

#Print out how many words were misspelled and the total number of words
print ('There were ' + str(count) + ' misspelled words out of ' + str(total_count) + '.')


