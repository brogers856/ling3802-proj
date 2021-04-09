import nltk
import tokenizer
import spellcheck

#Extracts features from email
def extract_features(data, spam_tokens):
    features = {}
    count = {}
    #Get counts of tokens
    tokenizer.tokenize(data, count)
    #Add features for tokens in top 300 spam tokens
    for key, value in spam_tokens:
        features[key] = key in count
    #Add feature for typo proportion
    features['typos'] = spellcheck.typo_proportion(data)
    return features

#Build decision tree
def build_tree(data, spam_tokens):
    featuresets = []
    i = 0
    #Extract features for each email
    for n in data:
        featuresets.append((extract_features(n, spam_tokens), data[n]))
        print("Extracting features: %d" % i, end="\r")
        i = i + 1

    print("\nTraining model...")
    #Train model
    classifier = nltk.DecisionTreeClassifier.train(featuresets, entropy_cutoff=0.05, depth_cutoff=50, support_cutoff=10, binary=True)
    return classifier