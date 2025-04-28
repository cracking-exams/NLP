# identify semantic relation between words(using word net)

import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

def describe(word):
    synets = wordnet.synsets(word)
    synonyms = {lemma.name() for syn in synets for lemma in syn.lemmas()}

    antonyms = {ant.name() for syn in synets for lemma in syn.lemmas() for ant in lemma.antonyms()}

    hyponyms = {hyp.name().split('.')[0] for syn in synets for hyp in syn.hyponyms()}

    hypernyms = {hyper.name().split('.')[0] for syn in synets for hyper in syn.hypernyms()}

    print(f"Word: {word}")
    print(f"Synonyms: {synonyms}")
    print(f"Antonyms: {antonyms}")
    print(f"Hypernyms: {hypernyms}")
    print(f"Hyponyms: {hyponyms}")

describe('car')
