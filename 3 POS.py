#3 Implement Part of Speech Tagging 

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tag_meaning = {
    'PRP':"Pronun",
    'VBP':'Verb',
    'RB':'Adverb',
    'JJ': 'Adjective',
    'NN':'Noun',
    'NNP':'Proper Noun',
    'VBZ': '(Verb 3rd person singular)',
    'VBG':'Verb (gerund/present participl)'
}

text = 'He is playing Cricket'
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# print(tags)

for word,tag in tags:
    meaning = tag_meaning.get(tag)
    print(f"{word} -> {tag} {meaning}")
