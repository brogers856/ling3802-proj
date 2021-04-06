import os

def read_items(spam_items, ham_items):
    for filename in os.listdir('data'):
        with open(os.path.join('data', filename), errors='ignore') as file:
            if 'spam' in filename:
                spam_items[file.read()] = 'spam'
            else:
                ham_items[file.read()] = 'ham'

def split_data(train, test, spam, ham):
    spam_size = len(spam)
    ham_size = len(ham)
    spam_items = list(spam.items())
    ham_items = list(ham.items())
    train.update(spam_items[:(int(spam_size*0.7))] + ham_items[:(int(ham_size* 0.7))])
    test.update(spam_items[(int(spam_size*0.7)):] + ham_items[(int(ham_size* 0.7)):])

