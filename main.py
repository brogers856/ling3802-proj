from __future__ import division
from pprint import pprint
import tokenizer
import splitter
import decisiontree


def prettyprint(count):
    print("====== Token Counts =======")
    for key in count:
        print(f"{count[key]}\t{key.rjust(3)}")


#count = {}
#tokenizer.read_data(count)
#pprint(list(sorted(count.items(), key=lambda x:x[1], reverse=True))[:300])

spam_items = {}
ham_items = {}
splitter.read_items(spam_items, ham_items)

train = {}
test = {}
splitter.split_data(train, test, spam_items, ham_items)

classifier = decisiontree.build_tree(train)

count = 0
for key, value in test.items():
    result = classifier.classify(decisiontree.extract_features(key))
    if result == value:
        count = count + 1

accuracy = count / len(test)
print('Accuracy: %f' % accuracy)

