import csv
import sys
import operator
from decimal import *

csv.field_size_limit(sys.maxsize)

extracts = list(csv.reader(open('corenlp_1000.csv.sub.extract.txt', 'rb'), delimiter='\t'))
confidence = Decimal(0.5)
nouns = dict()
actions = dict()
objects = dict()
triples = dict()

for entry in extracts:
	if Decimal(entry[len(entry)-7]) >= Decimal(confidence):
		if entry[len(entry)-3] in nouns:
			nouns[entry[len(entry)-3]] += 1
		else:
			nouns[entry[len(entry)-3]] = 1

		if entry[len(entry)-2] in actions:
			actions[entry[len(entry)-2]] += 1
		else:
			actions[entry[len(entry)-2]] = 1

		if entry[len(entry)-1] in objects:
			objects[entry[len(entry)-1]] += 1
		else:
			objects[entry[len(entry)-1]] = 1

		tip = entry[len(entry)-3] + " " + entry[len(entry)-2] + " " + entry[len(entry)-1];
		if tip in triples:
			triples[tip] += 1
		else:
			triples[tip] = 1
		
sortednouns = sorted(nouns.items(), key=operator.itemgetter(1))
sortedactions = sorted(actions.items(), key=operator.itemgetter(1))
sortedobjects = sorted(objects.items(), key=operator.itemgetter(1))
sortedtriples = sorted(triples.items(), key=operator.itemgetter(1))

print "Top 10 Nouns"
for i in range(1,11):
	print sortednouns[len(sortednouns)-i]
print "\nTop 10 Actions"
for i in range(1,11):
	print sortedactions[len(sortedactions)-i]
	
print "\nTop 10 Objects"
for i in range(1,11):
	print sortedobjects[len(sortedobjects)-i]

print "\nTop 10 Triple"
for i in range(1,11):
	print sortedtriples[len(sortedtriples)-i]
	
output = open('noun-freq-corenlp.txt', 'w')
output.write("Nouns Frequency \n")
for noun in sortednouns:
	output.write(noun[0] + "," + str(noun[1]) + "\n")
output.close()

output = open('action-freq-corenlp.txt', 'w')
output.write("Actions Frequency \n")
for actions in sortedactions:
	output.write(actions[0] + "," + str(actions[1]) + "\n")
output.close()

output = open('object-freq-corenlp.txt', 'w')
output.write("Objects Frequency \n")
for objects in sortedobjects:
	output.write(objects[0] + "," + str(objects[1]) + "\n")
output.close()

output = open('triple-freq-corenlp.txt', 'w')
output.write("Triples Frequency \n")
for triples in sortedtriples:
	output.write(triples[0] + "," + str(triples[1]) + "\n")	
output.close()