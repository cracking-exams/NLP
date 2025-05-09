#5 Implement ngram model

from nltk import ngrams

sentence = "I love NLP very much".split()

# Unigrams
unigrams = list(ngrams(sentence, 1))
print("Unigrams:", unigrams)

# Bigrams
bigrams = list(ngrams(sentence, 2))
print("Bigrams:", bigrams)

# Trigrams
trigrams = list(ngrams(sentence, 3))
print("Trigrams:", trigrams)
