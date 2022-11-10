import spacy

nlp = spacy.load("en_core_web_sm")

text =  open('dataset.txt', 'r')

doc = nlp(text.read())
# doc = nlp(u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)

# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# for entity in doc.ents:
#     print(entity.text, entity.label_)