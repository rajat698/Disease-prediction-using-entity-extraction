import spacy

nlp = spacy.load("en_core_web_sm")
raw_text=open('dataset.txt', 'r')

text1= nlp(raw_text)
for word in text1.ents:
    print(word.text,word.label_)
