from __future__ import division
from pprint import pprint
import tokenizer
import splitter
import decisiontree
import pickle

#Get user input to determine if model should be retrained
userinput = ''
while userinput != '1' and userinput != '2':
    userinput = input('Enter 1 to train new model, 2 to load saved model\n')

#Get counts of all tokens in spam emails
count = {}
tokenizer.read_data(count)
#Get top 300 most common tokens
spam_tokens = list(sorted(count.items(), key=lambda x:x[1], reverse=True))[:300]

#Split the data into two groups, one consisting of only spam, the other of only ham
spam_items = {}
ham_items = {}
splitter.read_items(spam_items, ham_items)

print("Splitting datasets...")

#Split the data 70/30 into training and testing sets
train = {}
test = {}
splitter.split_data(train, test, spam_items, ham_items)

if userinput == '1':
    #Build the decision tree
    classifier = decisiontree.build_tree(train, spam_tokens)
elif userinput == '2':
    #Load decision tree
    f = open('decision_tree_classifier', 'rb')
    classifier = pickle.load(f)
    f.close()
    print("Model loaded...")

tp = 0
fp = 0
tn = 0
fn = 0
i = 0
#Test all items in the test set
for key, value in test.items():
    result = classifier.classify(decisiontree.extract_features(key, spam_tokens))
    if result == 'spam' and value == 'spam':
        tp = tp + 1
    elif result == 'ham' and value == 'ham':
        tn = tn + 1
    elif result == 'spam' and value == 'ham':
        fp = fp + 1
    elif result == 'ham' and value == 'spam':
        fn = fn + 1
    print("Testing data: %d" % i, end="\r")
    i = i +1

#Print results info
accuracy = (tp + tn) / len(test)
print('Accuracy: %f' % accuracy)
print('Predicted correctly: %d' % (tp + tn))
print('Out of: %d' % (len(test)))
print('True positives: %d' % tp)
print('False positives: %d' % fp)
print('True negatives: %d' % tn)
print('False negatives: %d' % fn)

print(classifier.pseudocode(depth=4))

#Save the model
f = open('decision_tree_classifier', 'wb')
pickle.dump(classifier, f)
f.close()

