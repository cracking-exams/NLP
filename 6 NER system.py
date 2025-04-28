import spacy
from sklearn.metrics import precision_score,f1_score,recall_score
nlp = spacy.load('en_core_web_sm')

text = 'Narendra Modi was born in Gujrat.'

true_entites = [
    ('Narendra Modi','PERSON'),
    ('Gujrat','GPE')
]

doc =nlp(text)

predicted_entities = [(entity.text,entity.label_) for entity in doc.ents]

print(f'True Entites: {true_entites}')
print(f'Predicted Entites: {predicted_entities}')

true_labels = [label for _,label in true_entites]
pred_labels = [label for _,label in predicted_entities]


# Calculate Precision, Recall, and F1-Score
precision = precision_score(true_labels, pred_labels, average='macro', zero_division=1)
recall = recall_score(true_labels, pred_labels, average='macro', zero_division=1)
f1 = f1_score(true_labels, pred_labels, average='macro', zero_division=1)

print("\nEvaluation Metrics:")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
