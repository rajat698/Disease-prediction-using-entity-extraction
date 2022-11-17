import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example
import entities

nlp = spacy.load("en_core_web_sm")
ner=nlp.get_pipe("ner")
ner

#Function to train diseases, symptopms and treatments
def diseaseTrainer():
  train_disease = entities.entitiesSet()

  for i, annotations in train_disease:
    for ent in annotations.get("entities"):
      ner.add_label(ent[2])

  pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
  unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

  with nlp.disable_pipes(*unaffected_pipes) :
 
    sizes = compounding(1.0, 4.0, 1.001)
        
    for i in range(1000):
     
      random.shuffle(train_disease)
      batches = minibatch(train_disease, size=sizes)
      losses = {}
      for batch in batches:
        for text, annotations in batch:
          doc = nlp.make_doc(text)
          example = Example.from_dict(doc, annotations)
          nlp.update([example], drop=0.5, losses=losses)
          print("Losses",losses)

print("Trainer running")
diseaseTrainer()

text =  open('dataset.txt', 'r')
doc = nlp(text.read())

tags = []

for ent in doc.ents:
  if ent.label_ == 'DISEASE':
    if (ent.text, ent.label_) not in tags:
      tags.append((ent.text, ent.label_))
  
  else:
    tags.append((ent.text, ent.label_))

for i in tags:
  if not i[0].isdigit() or i[0].startswith('https:'):
    print(i[0],'-', i[1], '\n')