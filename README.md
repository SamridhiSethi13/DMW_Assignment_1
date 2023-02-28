# DMW_Assignment_1

### QUESTION - Implement Apriori Algorithm using python  

The Apriori algorithm is a popular algorithm for frequent itemset mining and association rule learning.  

In the implementation, I have considered **min_support = 0.6 (60%)**  
 
<br>
 
*Result of implementing this algorithm on the dataset used (transactions.csv)*  

C1:  
{'A': 0.5, 'C': 0.75, 'D': 0.25, 'B': 0.75, 'E': 0.75}  
  
L1:  
C : 0.75  
B : 0.75  
E : 0.75  
  
C2:  
{('B', 'C'): 0.5, ('B', 'E'): 0.75, ('C', 'E'): 0.5}  
  
L2:  
('B', 'E') : 0.75  
  
C3:  
{}  
  
L3:  
  
Final Frequent Set  
[('B', 'E')]
