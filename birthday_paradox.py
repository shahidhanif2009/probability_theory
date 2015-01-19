'''
Created on 19 Jan 2015
Birthday Paradox
This script proves the theoratical formula is true and draws 
the same nice curve as in wikipedia.

@author: shaihid
'''
import random
from collections import Counter
import matplotlib.pyplot as plt

minN = 1;
maxN = 100;
maxTests = 10000;

probabilities = []                # to store the probability for each n population
for n in range(minN,maxN+1):    #try every n for t times
    
    found = 0                   #Increment by one when duplicates of any birthday is greater than 1
    for t in range(maxTests+1):
        #create n random int between 1 and 366
        random_birthdates = [random.randint(1,366) for counter in xrange(n)]
        #count maximum duplicates of any birthday in random_birthdates
        freq = len([k for k,v in Counter(random_birthdates).items() if v>1])
        if freq > 0:
            found  = found + 1
    
    probabilities += [found*1.0/maxTests]


plt.title("Birthday Pradox")
plt.xlabel("Population size")
plt.ylabel("Probability")
plt.ylim(0,1);
plt.plot([x for x in range(minN, maxN+1)], probabilities)    
plt.savefig("birthday_paradox.png")
