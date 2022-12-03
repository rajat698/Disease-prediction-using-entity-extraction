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
        
    for i in range(100):
     
      random.shuffle(train_disease)
      batches = minibatch(train_disease, size=sizes)
      losses = {}
      for batch in batches:
        for text, annotations in batch:
          doc = nlp.make_doc(text)
          example = Example.from_dict(doc, annotations)
          nlp.update([example], drop=0.5, losses=losses)
          print("Losses",losses)

dictSymptoms = {}
dictTreatments = {}
tags = []

#Function to save disease and their symtoms, treatments in a dictionary
def makeTags():


  text =  open('text.txt', 'r')
  
  doc = nlp(text.read())
  

  for ent in doc.ents:
    if not ent.text.isdigit() and not ent.text.startswith('https:') and ent.label_ == 'DISEASE':
      if (ent.text, ent.label_) not in tags:
        tags.append((ent.text, ent.label_))
    
    else:
      tags.append((ent.text, ent.label_))

  #Making a dictionary for symptopms
  tempSym = 'default'
  for i in tags:
    if i[1] == 'DISEASE':
      dictSymptoms[i[0]] = ''
      tempSym = i[0]
    
    elif i[1] == 'SYMPTOM':
      if tempSym != 'default':
        if len(dictSymptoms[tempSym]) == 0:
          dictSymptoms[tempSym] = i[0]

        else:    
          dictSymptoms[tempSym] = dictSymptoms[tempSym] + ', ' + i[0]

  for key in dictSymptoms.keys():
    if dictSymptoms[key] == '':
      dictSymptoms[key] = 'No particualar symptom. Doctor\'s diagnosis required.'

  #Making a dictionary for treatments
  tempTre = 'default'
  for i in tags:
    if i[1] == 'DISEASE':
      dictTreatments[i[0]] = ''
      tempTre = i[0]
    
    elif i[1] == 'TREATMENT':
      if tempTre != 'default':
        if len(dictTreatments[tempTre]) == 0:
          dictTreatments[tempTre] = i[0]

        else:    
          dictTreatments[tempTre] = dictTreatments[tempTre] + ', ' + i[0]

  
  for key in dictTreatments.keys():
      if dictTreatments[key] == '':
        dictTreatments[key] = 'No particualar Treatment. Doctor\'s prescription required.'
  
#Main Function
def main():
  diseaseTrainer()
  makeTags()

if __name__ == '__main__':
  main() 