# Lab 22: Part 1 — Predictions

## Prediction 1: Which variant breaks first as input size grows? Why?

Solution C would most likely break first because it uses a simple for loop to count the number of times each item appears in the list. This means for each item the program needs to walk through the entire list to count the number of times that item appears. This means a high time complexity of O(n^2) I believe.

## Prediction 2: Which variant would you trust to run at 3am during an outage? "Trust" can mean speed, readability, edge-case handling — name what you mean.

For me I would trust solution_a. It is the most readable with a less amount of code written. It uses the Counter class which is built for manually counting items in a list rather than building that function yourself. It also uses the heapq.nlargest function to get the most frequent items instead of building that function yourself as well.# Lab 22 Writeup

## Part 1: Predict Before You Test

### Solution A

The goal is to form a  new list with the most frequent values listed from first to last. 
Fist the program checks if the list is empty then moves to count the frequency of each item using the Counter class.
Then the prrogram creates a list of tuples with their count, their index and the item itself. The program then uses
the heapq.nlargest function to get the most frequent items based on their count and uses the index for tiebreak.
Finally the function returns a list of tuples with the most frequent values listed first.

Prediction 1: Which variant breaks first as input size grows? Why?
solution_c would most likely break first because it uses a simple for loop to count the number of times each item appears
in the list. This means for each item the preogram needs to walk through the eniter list to count the number of times that item appears.
this means a high time complexity of O(n^2) I belive.

Prediction 2: Which variant would you trust to run at 3am during an outage? "Trust" can mean speed, readability, edge-case handling — name what you mean.
For me I would trust solution_a. I is the most readble with a less amount of code written. It uses the counter class which is boilt for manually counting items in a list
rather than build that function youself. It also uses the heapq.nlargest function to get the most frequent items istead of building that function yourself as well.

### Solution B

In soulution_b the program again checks if the list is empty. then uses the same counter method to count the items in the list.
Then the program creates a list of tuples with the item, its count and its index. The program then sorts the list of tuples by 
count using a lambda function this time. Finally the function returns a list of tuples with the most frequent values listed first.

Prediction 1: 

Prediction 2: 

### Solution C

 for soultion_c the program again checks if the list is empty. There is then a list of the seen order and a set of seen items. 
the program walk through the list and adds the item to the seen set and the seen order list if the item has noit been seen before.
The a list of tuples is created with the item and its count. for each item is the seen order the list program counts the number of times it comes up 
in the list and appends the item and the count to the list of tuples. Finaly the list of tuples is soreted by count using a lambda function
and top k items are returned.

Prediction 1: 

Prediction 2: 