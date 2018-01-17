#A script to count the number of times a journal appears in your bibtex bibliography
#Handy for selecting journals to publish in!


import collections

with open('Bibliography.bib') as infile:
    counts = collections.Counter(line.strip() for line in infile)
for line, count in counts.most_common():
    #print (line, count)
    if line.startswith('journal'):
        print(line, count)
