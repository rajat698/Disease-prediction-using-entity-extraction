import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")
ner=nlp.get_pipe("ner")
ner

#Function to train diseases
def diseaseTrainer():
  text_disease = open('diseasedata.txt', 'r').read()
  train_disease = [(text_disease , {"entities": [(654,661, 'DISEASE'),(1890,1896, 'DISEASE'),(2311,2323, 'DISEASE'),
                                              (1382,1391, 'DISEASE'), (406,414, 'DISEASE'), 
                                              (2539,2543, 'DISEASE'), (168,177, 'DISEASE'),
                                            (2325,2327, 'DISEASE'), (518,524, 'DISEASE'),(3028,3038,'DISEASE'),(3101,3110, 'DISEASE'),
                                              (3264,3268, 'DISEASE'), (3360,3364, 'DISEASE'), (3494,3507, 'DISEASE'),
                                              (3600,3612, 'DISEASE'), (3683,3689, 'DISEASE'), (3736,3757, 'DISEASE')
                                              , (3874,3885, 'DISEASE'), (4044,4051, 'DISEASE'), (4145,4184, 'DISEASE'), (4326,4334, 'DISEASE'),
                                              (4450,4462, 'DISEASE'), (4551,4558, 'DISEASE'), (4638,4648, 'DISEASE'),
                                              (4763, 4773, 'DISEASE'), (5613, 5621, 'DISEASE'), (7250, 7258, 'DISEASE'), (5405,5414, 'SYMPTOPM'), (5512, 5520, 'SYMPTOPM'), (6825, 6832, 'SYMPTOPM'),
                    (6847, 6856, 'SYMPTOPM'), (6910, 6917, 'SYMPTOPM'), (7057, 7062, 'SYMPTOPM'), (7067, 7071, 'SYMPTOPM'),
                    (7195, 7205, 'SYMPTOPM'), (8063, 8071, 'SYMPTOPM'), (8099, 8103, 'SYMPTOPM'), (8134, 8139, 'SYMPTOPM'), (8142, 8148, 'SYMPTOPM'), (8153, 8161, 'SYMPTOPM')]})]

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


def symptopmsTrainer():
  text_symptoms = open('diseasedata.txt', 'r').read()
  train_symptopms = [(text_symptoms, {"entities": [(5405,5414, 'SYMPTOPM'), (5512, 5520, 'SYMPTOPM'), (6825, 6832, 'SYMPTOPM'),
                    (6847, 6856, 'SYMPTOPM'), (6910, 6917, 'SYMPTOPM'), (7057, 7062, 'SYMPTOPM'), (7067, 7071, 'SYMPTOPM'),
                    (7195, 7205, 'SYMPTOPM')]})]

  for i, annotations in train_symptopms:
    for ent in annotations.get("entities"):
      ner.add_label(ent[2])

  pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
  unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

  with nlp.disable_pipes(*unaffected_pipes) :
 
    sizes = compounding(1.0, 4.0, 1.001)
        
    for i in range(100):
     
      random.shuffle(train_symptopms)
      batches = minibatch(train_symptopms, size=sizes)
      losses = {}
      for batch in batches:
        for text, annotations in batch:
          doc = nlp.make_doc(text)
          example = Example.from_dict(doc, annotations)
          nlp.update([example], drop=0.5, losses=losses)
          print("Losses",losses)

print("diseaseTrainer running")
diseaseTrainer()
print("\nsymptopmsTrainer running")
# symptopmsTrainer()

text =  open('dataset.txt', 'r')
doc = nlp(text.read())

for ent in doc.ents:
  print(ent.text,'-', ent.label_,'\n')