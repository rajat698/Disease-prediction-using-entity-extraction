text_disease = open('diseasedata.txt', 'r').read()
string = text_disease
x = 'Rash'
index = string.rindex(x)
print(index, index + len(x))