cd C:\Users\biega\Disease-prediction-using-entity-extraction
python symptomsCSV.py
javac PrepareDataInsert.java
java PrepareDataInsert
javac -cp ".;C:\Users\biega\apache-jena-4.6.1\lib\*" MedicalConditions.java
java -cp ".;C:\Users\biega\apache-jena-4.6.1\lib\*" MedicalConditions update
exit