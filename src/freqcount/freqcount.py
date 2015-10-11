import csv
import sys
import operator

csv.field_size_limit(sys.maxsize)

extracts = list(csv.reader(open('1000_extract.txt', 'rb'), delimiter='\t'))

nouns = dict()
actions = dict()
objects = dict()
triples = dict()

for entry in extracts:
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
