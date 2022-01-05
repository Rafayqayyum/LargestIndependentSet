
import itertools
import pandas as pd
import numpy as np
import random

#calculates all the powersets
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item

#checks if the set is independent
def isIndependent(sub, edge):
    for i in range(0, len(sub)):
        for j in range(i, len(sub)):
            if edge[sub[i]][sub[j]] == 1 or edge[sub[j]][sub[i]] == 1:
                return False
    return True

#returns the largest independent set
def getIndependentSet(set, edge):
    largest = []
    subsets = [x for x in powerset(set)]
    random.shuffle(subsets)
    for sub in subsets:
        if isIndependent(sub, edge):
            if len(sub) > len(largest):
                largest = sub
    return largest



set = [1, 2, 3, 4, 5, 6, 7]
#generates a length(set) x length(set) matrix with ones and zeros
#to creates edges in the graph
array = np.random.randint(0, 2, size=(len(set), len(set)))

#makes the edges in directed by placing 1s at ji index for every ij index
#and removes the self edge from the graphs
for i in range(0, len(set)):
    for j in range(0, len(set)):
        if array[i][j] == 1 and i != j:
            array[j][i] = 1
        if i == j:
            array[i][j] = 0

#creates a pandas dataframe for the graph
df = pd.DataFrame(array, columns=set, index=set)


res= getIndependentSet(set, df)
print('Largest independent set is: ',res)
#prints the edges matrix on the screen
print('\nThe edge matrix is: \n')
print (df)
