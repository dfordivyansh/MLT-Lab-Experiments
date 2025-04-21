## Implement  and  demonstrate  the  FIND-S  algorithm  for  finding  the  most  specific hypothesis  based  on  a  given  set  of  training  data  samples.  Read  the  training  data  from  a  .CSV file. 

**FIND-S  Algorithm**
```
1.  Initialize  h  to  the  most  specific  hypothesis  in  H 
2.  For  each  positive  training  instance  x 
3.     For  each  attribute  constraint  ai  in  h 
4.        If  the  constraint  ai  is  satisfied  by  x 
5.              Then  do  nothing 
6.        Else  replace  ai  in  h  by  the  next  more  general  constraint  that  is  satisfied  by  x 
7.  Output  hypothesis  h
```

### To illustrate this algorithm, assume the learner is given the sequence of training examples from the EnjoySport task


| Example | Sky    | AirTemp | Humidity  | Wind    | Water | Forecast  | EnjoySport  |
| ------- | ------ | ------- | --------  | ------- | ----- | --------  | ----------  |
| 1       | Sunny  | Warm    | Normal    | Strong  | Warm  | Same      | Yes         |
| 2       | Sunny  | Warm    | High      | Strong  | Warm  | Same      | Yes         |
| 3       | Rainy  | Cold    | High      | Strong  | Warm  | Change    | No          |
| 4       | Sunny  | Warm    | High      | Strong  | Cool  | Change    | Yes         |


• The first step of FIND-S is to initialize h to the most specific hypothesis in H

**h - (Ø, Ø, Ø, Ø, Ø, Ø)**
------------------------------------------------------------------------
**Consider the first training example**

**x1 = [Sunny Warm Normal Strong Warm Same], +**

Observing the first training example, it is clear that hypothesis h is too specific. 

None of the "Ø" constraints in h are satisfied by this example, so each is replaced by the next more general constraint that fits the example

**h1 = [Sunny Warm Normal Strong Warm Same]**

------------------------------------------------------------------------

**Consider the second training example**

**x2 = [Sunny, Warm, High, Strong, Warm, Same], +**

The second training example forces the algorithm to further generalize h, this time substituting a "?" in place of any attribute value in h that is not satisfied by the new example

**h2 = [Sunny Warm ? Strong Warm Same]**

------------------------------------------------------------------------

**Consider the third training example**

**x3 = [Rainy, Cold, High, Strong, Warm, Change], -**

Upon encountering the third training the algorithm makes no change to h. Because the FIND-S algorithm simply ignores every negative example.

**h3 =  [Sunny Warm ? Strong Warm Same]**

------------------------------------------------------------------------
**Consider the fourth training example**

**x4 =  [Sunny Warm High Strong Cool Change], +**

The fourth example leads to a further generalization of h

**h4 = [Sunny Warm ? Strong ? ? ]**

------------------------------------------------------------------------
### Code

```python

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
```

------------------------------------------------------------------------
### Output
```
[['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'], ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'], 
['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'], ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']]

 The total number of training instances are :  4

 The initial hypothesis is : 
 ['0', '0', '0', '0', '0', '0']

 The hypothesis for the training instance 1 is: 
 ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']

 The hypothesis for the training instance 2 is: 
 ['sunny', 'warm', '?', 'strong', 'warm', 'same']

 The hypothesis for the training instance 3 is: 
 ['sunny', 'warm', '?', 'strong', 'warm', 'same']

 The hypothesis for the training instance 4 is: 
 ['sunny', 'warm', '?', 'strong', '?', '?']

 The Maximally specific hypothesis for the training instances is: 
 ['sunny', 'warm', '?', 'strong', '?', '?']
```
