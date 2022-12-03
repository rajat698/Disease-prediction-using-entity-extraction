import app
from app import dictSymptoms
from app import dictTreatments
import csv
import pandas as pd

# app.giveTags()
app.main()

#Making .csv file for symptoms triples
with open('symptoms.csv', 'w', newline = '') as f:

  write = csv.writer(f)
  write.writerow(['Disease', 'Symptom', 'Property'])  

  for key in dictSymptoms.keys():
    write.writerow([key, dictSymptoms[key], 'hasSymptom'])

#Making .csv file for treatments triples
with open('treatment.csv', 'w', newline = '') as f:

  write = csv.writer(f)
  write.writerow(['Disease', 'Treatment', 'Property'])  

  for key in dictTreatments.keys():
    write.writerow([key, dictTreatments[key], 'hasTreatment'])

