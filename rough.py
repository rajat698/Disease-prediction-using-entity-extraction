import spacy
import random

nlp = spacy.blank('en')

nlp.vocab.vectors.name = 'example_model_training'

ner = nlp.add_pipe('ner')
# nlp.add_pipe('ner')

DATA = [
  (u"Search Analytics: Business Value & BigData NoSQL Backend, Otis Gospodnetic ", {'entities': [ (58,75,'PERSON') ] }),
  (u"Introduction to Elasticsearch by Radu ", {'entities': [ (16,29,'TECH'), (32, 36, 'PERSON') ] }),
]

nlp.ents.add_label('PERSON')
nlp.entity.add_label('TECH')

optimizer = nlp.begin_training()

for i in range(20):
    random.shuffle(DATA)
    for text, annotations in DATA:
        nlp.update([text], [annotations], sgd=optimizer)

doc = nlp(u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)