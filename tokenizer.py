import nltk
import os
nltk.download('punkt')

def tokenize(data, count):
    tokens = nltk.word_tokenize(data)

    for token in tokens:
        if token in count.keys():
            count[token] = count[token] + 1
        else:
            count[token] = 1

def read_data(count):
    for filename in os.listdir('data'):
        with open(os.path.join('data', filename), errors='ignore') as file:
            if 'spam' in filename:
                data = file.read()
                tokenize(data, count)
 