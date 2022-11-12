import spacy
import re
import random
from spacy.util import minibatch, compounding
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")
ner=nlp.get_pipe("ner")
ner
text_disease = open('diseasedata.txt', 'r').read()
train_disease = [(text_disease , {"entities": [(654,661, 'DISEASE'),(1890,1896, 'DISEASE'),(2311,2323, 'DISEASE'),
                                            (1382,1391, 'DISEASE'), (406,414, 'DISEASE'), 
                                            (2539,2543, 'DISEASE'), (168,177, 'DISEASE'),
                                           (2325,2327, 'DISEASE'), (518,524, 'DISEASE'),(3028,3038,'DISEASE'),(3101,3110, 'DISEASE'),
                                            (3264,3268, 'DISEASE'), (3360,3364, 'DISEASE'), (3494,3507, 'DISEASE'),
                                            (3600,3612, 'DISEASE'), (3683,3689, 'DISEASE'), (3736,3757, 'DISEASE')
                                            , (3874,3885, 'DISEASE'), (4044,4051, 'DISEASE'), (4145,4184, 'DISEASE'), (4326,4334, 'DISEASE'),
                                            (4450,4462, 'DISEASE'), (4551,4558, 'DISEASE'), (4638,4648, 'DISEASE')]})]

for i, annotations in train_disease:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*unaffected_pipes) :
 
   sizes = compounding(1.0, 4.0, 1.001)
        
   for itn in range(1000):
     
     random.shuffle(train_disease)
     batches = minibatch(train_disease, size=sizes)
     losses = {}
     for batch in batches:
       for text, annotations in batch:
         doc = nlp.make_doc(text)
         example = Example.from_dict(doc, annotations)
         nlp.update([example], drop=0.5, losses=losses)
         print("Losses",losses)

text =  open('dataset.txt', 'r')
doc = nlp(text.read())

string = text_disease
# match = re.search("Asbestosis", string)
# print('%d,%d' % (match.start(), match.end()))

for ent in doc.ents:
  print(ent.text,'-', ent.label_,'\n')