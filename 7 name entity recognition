# 7. Perform named entity recognition on a given text

import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple Inc. is looking at buying U.K. startup for $1 billion." #replace with the given text
doc = nlp(text)

for ent in doc.ents: 
    print(ent.text, "->", ent.label_)
