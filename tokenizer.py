import nltk
import os
nltk.download('punkt')

#Tokenize email and count tokens
def tokenize(data, count):
    #Get all tokens
    tokens = nltk.word_tokenize(data)

    for token in tokens:
        #If token already in dict, increment it's count. Else, add to the dict
        if token in count.keys():
            count[token] = count[token] + 1
        else:
            count[token] = 1

#Read in data of spam emails
def read_data(count):
    i = 0
    for filename in os.listdir('data'):
        with open(os.path.join('data', filename), errors='ignore') as file:
            if 'spam' in filename:
                data = file.read()
                tokenize(data, count)
        print("Reading data: %d" % i, end="\r")
        i = i +1
 