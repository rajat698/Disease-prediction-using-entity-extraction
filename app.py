import spacy

nlp = spacy.load("en_core_web_sm")

text =  open('dataset.txt', 'r')

doc = nlp(text.read())

for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)

# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# for entity in doc.ents:
#     print(entity.text, entity.label_)