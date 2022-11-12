# a = [('Asbestosis', 'DISEASE'), ('Asbestosis', 'DISEASE'), ('Aspergillosis', 'DISEASE'), ('Impetigo', 'DISEASE'), ('Agoraphobia', 'DISEASE'), ('Agoraphobia', 'DISEASE'), ('Amenorrhea', 'DISEASE'), ('cancer', 'DISEASE'), ('Angiosarcoma', 'DISEASE'), ('Aphasia', 'DISEASE'), ('Aphasia', 'DISEASE'), ('Appendicitis', 'DISEASE'), ('Brucellosis', 'DISEASE'), ('Cervicitis', 'DISEASE'), ('Cholecystitis', 'DISEASE'), ('Epilepsy', 'DISEASE'), ('Gangrene', 'DISEASE'), ('Hemophilia', 'DISEASE'), ('Hypoglycemia', 'DISEASE'), ('Kleptomania', 'DISEASE'), ('Kleptomania', 'DISEASE'), ('XLA', 'DISEASE'), ('XLA', 'DISEASE'), ('XLA', 'DISEASE'), ('cancer', 'DISEASE'), ('Saliva', 'DISEASE'), ('WPWsyndrome', 'DISEASE'), ('Tachycardia', 'DISEASE'), ('Tachycardia', 'DISEASE'), ('Tuberculosis', 'DISEASE'), ('AIDS', 'DISEASE')]
# sum = 0
# for i in a:
#     sum += 1
# print(sum)
import re

text_disease = open('diseasedata.txt', 'r').read()
string = text_disease
match = re.search("varicocele", string)
print('%d,%d' % (match.start(), match.end()))