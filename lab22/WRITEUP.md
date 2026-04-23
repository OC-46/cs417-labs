Part 1:

solution_a-The goal is to form a  new list with the most frequent values listed from first to last. 
Fist the program checks if the list is empty then moves to count the frequency of each item using the Counter class.
Then the prrogram creates a list of tuples with their count, their index and the item itself. The program then uses
the heapq.nlargest function to get the most frequent items based on their count and uses the index for tiebreak.
Finally the function returns a list of tuples with the most frequent values listed first.

solution_b-In soulution_b the program again checks if the list is empty. then uses the same counter method to count the items in the list.
Then the program creates a list of tuples with the item, its count and its index. The program then sorts the list of tuples by 
count using a lambda function this time. Finally the function returns a list of tuples with the most frequent values listed first.


solution_c- for soultion_c the program again checks if the list is empty. There is then a list of the seen order and a set of seen items. 
the program walk through the list and adds the item to the seen set and the seen order list if the item has noit been seen before.
The a list of tuples is created with the item and its count. for each item is the seen order the list program counts the number of times it comes up 
in the list and appends the item and the count to the list of tuples. Finaly the list of tuples is soreted by count using a lambda function
and top k items are returned.

Predictions

Prediction 1: Which variant breaks first as input size grows? Why?
solution_c would most likely break first because it uses a simple for loop to count the number of times each item appears
in the list. This means for each item the preogram needs to walk through the eniter list to count the number of times that item appears.
this means a high time complexity of O(n^2) I belive.

Prediction 2: Which variant would you trust to run at 3am during an outage? "Trust" can mean speed, readability, edge-case handling — name what you mean.
For me I would trust solution_a. I is the most readble with a less amount of code written. It uses the counter class which is boilt for manually counting items in a list
rather than build that function youself. It also uses the heapq.nlargest function to get the most frequent items istead of building that function yourself as well.

Part 2:

For ranking these solutions, I would put solution_a as the best solution because it is the easiest to read for me.
It ueses the built in functions like the counter class and the heapq functions which are aready built for this type of problem. Solution_b is the second best soultion for me because it also uses built in functions but uses the sort function insead of heapq. This program is still good but I think the heapq function is better for this problem. Solution_c is the worst because it dosent take advantage of any of the built in functions avalible and istead builds the functions manually. this makes the code harder to undderstand and is more prone to breaking than the other functions. Also the time compexity is higher than the other solutions because of the nested loop. 

timing table
=== Regime 1 — small fixed vocabulary (50 distinct items) ===
         n |   unique |     A (heap) |     B (sort) |     C (loop)
------------------------------------------------------------------------
       100 |       50 |       0.10ms |       0.04ms |       0.13ms
     1,000 |       50 |       0.15ms |       0.11ms |       4.42ms
    10,000 |       50 |      10.81ms |       0.82ms |      30.34ms
   100,000 |       50 |      12.95ms |       9.49ms |      94.99ms

=== Regime 2 — vocabulary scales with n (unique ≈ n/2) ===
         n |   unique |     A (heap) |     B (sort) |     C (loop)
------------------------------------------------------------------------
       100 |       50 |       0.05ms |       0.03ms |       0.07ms
     1,000 |      500 |       0.15ms |       0.24ms |       9.02ms
    10,000 |    5,000 |       4.69ms |      13.25ms |     781.42ms

(.venv) @OC-46 ➜ /workspaces/cs417-labs/lab22 (main) $ mypy --strict src/solution_a.py src/solution_b.py src/solution_c.py
src/solution_c.py:29: error: Incompatible return value type (got "list[tuple[str, int]]", expected "list[int]")  [return-value]
Found 1 error in 1 file (checked 3 source files)

Part 3:

Yes the benchmark numbers confirmed what i predicted. It was pretty obvious that solution_c was going to perform the worst on both regimes as it did. Solution_b was acually much quicker when only dealing with 50 unique items but and the list of unique items grew solution_a ended up being the much faster choice. This shows that the sorting solution in b was slightly better when there was only 50 unique items no matter the number of items in that list but it was only slightly better than solution a. Solution_a was much than both b and c when it came to 5,000 unique characters making it the best option if you do not know how many unique characters you are dealing with or if you already know there are a lot that you have to deal with. The mypy caught an issue with solution_c as well where it got a tuple with a string and int iside istead of a list with ints inside from the retun value meaning the program is not return as it should be.

part 4:

Scenario A — small, infrequent. Input is guaranteed to be under 50 items. The function runs once a week in a cron job. Does your ranking from Part 2 change? Why or why not?

Yes in this case i would change the ranking and put solution_c above solution_a because the testing did show that this solution was quicker when the number of items are under 50 reqardless on how many are unique or not. Solution_a does see a consistetly higher time although its not by much and even with a very infrequent fun time this sill could be a decent option the run time and also simplicity of code that is written for solution_b would make this the right choice.

Scenario B — hot path. The function runs 10,000 times per second on the request path of a service. The workloads look like Regime 2 from the benchmark — many distinct items. Does your ranking change? What additional concerns surface that didn't matter in Scenario A?

MY ranking would stay the same for this scenario, It was pretty clear in the testing that scenario_a was much faster when it came to reqime 2. The heapq function is clearly better and hendling the much higher level of unique characters much better then either of the other options. This solution while still not quite being as simple as solution_b is, it is still pretty simple and cand be understood when reading though the code ofr the first time. If we are looking for good speed and can handle the sheer number or requests solution_a is the best for that.

