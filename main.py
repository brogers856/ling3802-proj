import nltk
import os
from pprint import pprint
nltk.download('punkt')

def prettyprint(count):
    print("====== Token Counts =======")
    for key in count:
        print(f"{count[key]}\t{key.rjust(3)}")

def tokenize(data, count):
    tokens = nltk.word_tokenize(data)

    for token in tokens:
        if token in count.keys():
            count[token] = count[token] + 1
        else:
            count[token] = 1

def read_data(count):
    for filename in os.listdir('data/enron1/spam'):
        with open(os.path.join('data/enron1/spam', filename), errors='ignore') as file:
            data = file.read()
            tokenize(data, count)
 

count = {}
read_data(count)

pprint(list(sorted(count.items(), key=lambda x:x[1], reverse=True))[:300])

