import app
from app import dict
import csv

app.giveTags()

with open('sympTriples.csv', 'w', newline = '') as f:

  write = csv.writer(f)
  write.writerow(['Disease', 'Symptom', 'Property'])  

  for key in dict.keys():
    write.writerow([key, dict[key], 'hasSymptom'])