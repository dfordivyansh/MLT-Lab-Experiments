
"""
Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis 
based on a given set of training data samples. Read the training data from a .CSV file

"""
import csv

a = []

with open('1.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)

print("\n The total number of training instances are : ",len(a))

num_attribute = len(a[0])-1

hypothesis = ['0']*num_attribute
print("\n The initial hypothesis is : \n", hypothesis)


for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is: \n" .format(i+1),hypothesis)

print("\n The Maximally specific hypothesis for the training instances is: \n",hypothesis )