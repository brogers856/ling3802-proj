import nltk
import tokenizer

#placeholders for now
spam_tokens = ['!', '$', "%", 'price', 'pills', 'stock', 'money', 'investment', 'security', 'click', 'product', 'product', 'offer', 'free', 'service', 'dollars']

def extract_features(data):
    features = {}
    count = {}
    tokenizer.tokenize(data, count)
    for token in spam_tokens:
        features[token] = token in count
    return features

def build_tree(data):
    featuresets = [(extract_features(n), data[n]) for n in data]
    classifier = nltk.DecisionTreeClassifier.train(featuresets)
    return classifier