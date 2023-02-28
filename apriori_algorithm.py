import pandas as pd
import numpy as np
import csv
# df = pd.read_csv("transactions.csv", header=None)
# print(df)

def load_data(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data 

df = load_data("transactions.csv")
df = pd.DataFrame(df)

from collections import Counter     #count the itemset in an iterable list,Counter holds the data in an unordered collection
from itertools import combinations        
Candidate_set = []
Frequent_set = []
itemset = pd.unique(df.values.ravel())   #unique values in column
itemset = itemset[~pd.isnull(itemset)]       #consider only not null itemset
min_support = 0.6
fl=0
no_of_transactions = df[df.columns[0]].count()

for it in range(1,len(itemset)+1): #Max iterations is equal to the itemset in the dataset
    Count = {}     
    intermediate = []   
    print("C"+str(it)+":")
    if it==1:
        Candidate_set.append(itemset)
        for txn in Candidate_set[it-1]:
            cntr=0
            for val in df.values:
                if txn in val:
                    cntr+=1
            Count[txn] = cntr/no_of_transactions
    else:
      if Frequent_set!=[]:
        Candidate_set.append(list(combinations(np.unique(np.array(Frequent_set[it-2]).ravel()),it)))
        for txn in Candidate_set[it-1]:
            cntr = 0
            for val in df.values:
                if all(i in val for i in txn):
                    cntr+=1
            Count[txn] = cntr/no_of_transactions
            
    for k in Count.keys():
        if Count[k] >= min_support:
            intermediate.append(k)       
  
    print(Count)
    print()
   
    print("L"+str(it)+":")
    for key,value in Count.items():
      if(value>=min_support):
        print(key,':',value)
    print()

    if intermediate == []:
        print('Final Frequent Set')
        if Frequent_set !=[]:
            print(Frequent_set[-1])
            fl=1
            break
        else:
            print("no such frequent set")
            fl=1
            break
    Frequent_set.append(intermediate)

if fl==0:
  if Frequent_set !=[]:
    print('Final Frequent Set:')
    print(Frequent_set[-1])
  else:
    print("no such frequent set")
