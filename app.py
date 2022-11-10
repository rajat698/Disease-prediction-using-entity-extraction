import spacy

nlp = spacy.load("en_core_web_sm")
ner=nlp.get_pipe("ner")
ner
text_disease = """Based on the statistics from WHO and the Centers for Disease Control and Prevention,here are the five most common infectious diseases.
According to current statistics, hepatitis B is the most common infectious disease in the world, affecting some 2 billion people -- that's more than one-quarter of the world's population. This disease, which is characterized by an inflammation of the liver that leads to jaundice, nausea, and fatigue, can lead to long-term complications such as cirrhosis of the liver or even liver cancer. The concern is primarily for those who carry the chronic form of the disease, which is estimated to be about 350 million people.Malaria, a mosquito-borne disease that tends to affect children the most in tropical and subtropical climates, affects more than 500 million people annually and results in anywhere between 1 million and 3 million deaths. Behind hepatitis B, it appears to be the second most-common infectious disease, and it certainly is one of the most deadly on an annual basis.
Malaria, a mosquito-borne disease that tends to affect children the most in tropical and subtropical climates, affects more than 500 million people annually and results in anywhere between 1 million and 3 million deaths. Behind hepatitis B, it appears to be the second most-common infectious disease, and it certainly is one of the most deadly on an annual basis.
Hepatitis C is a less common and less severe form of hepatitis, but it almost always develops into a chronic, not acute, condition, unlike hepatitis B. Although only 3 million to 4 million new cases are reported each year, some 180 million people worldwide suffer from this chronic condition, which can lead to liver cancer or cirrhosis of the liver over time.
It's at times like these that we curse mosquitoes, because a very specific type of mosquito (Aedes aegypti) is responsible for the transmission of dengue to approximately 50 million people each year. Dengue is most common in Africa and Asia and thankfully occurs in only mild to moderate forms, which can cause high fever, severe headaches, and joint and muscle pain, but rarely leads to the death of the infected patient.
As I mentioned previously, estimating new and ongoing cases for some of these diseases can be downright difficult, and perhaps none more so than tuberculosis. TB is caused by a bacteria found in the lungs that can cause chest pain and a bad cough, as well as lead to a number of other nasty side effects. According to WHO, it's also the second-leading global killer behind AIDS as a single infectious agent.The majority of TB-associated deaths (95%) occur in low- to middle-income countries where TB awareness and prevention simply aren't where they need to be. The good news is that TB death rates on a global basis are falling; however, there were still 8.6 million new cases of TB reported last year, and roughly one-third of the world's population carries a latent form of TB,
meaning they've been infected but aren't ill and can't transmit the disease yet. """
TRAIN_DATA = [(text_disease , {"entities": [(654,661, 'DISEASE'),(1890,1896, 'DISEASE'),(2311,2323, 'DISEASE'),
                                            (1382,1391, 'DISEASE'), (406,414, 'DISEASE'), 
                                            (2539,2543, 'DISEASE'), (168,177, 'DISEASE'),
                                           (2325,2327, 'DISEASE'), (518,524, 'DISEASE')]})]

for i, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
#import necessary libraries for training
import random
from spacy.util import minibatch, compounding
from spacy.training import Example
# Begin training by disabling other pipeline components
with nlp.disable_pipes(*unaffected_pipes) :
 
   sizes = compounding(1.0, 4.0, 1.001)
   # Training for 100 iterations     
   for itn in range(100):
     # shuffle examples before training
     random.shuffle(TRAIN_DATA)
     # batch up the examples using spaCy's minibatch
     batches = minibatch(TRAIN_DATA, size=sizes)
     # dictionary to store losses
     losses = {}
     for batch in batches:
       for text, annotations in batch:
         doc = nlp.make_doc(text)
         example = Example.from_dict(doc, annotations)
         nlp.update([example], drop=0.5, losses=losses)
         print("Losses",losses)

text =  open('dataset.txt', 'r')
doc = nlp(text.read())

print('Entities', [(ent.text, ent.label_) for ent in doc.ents])


