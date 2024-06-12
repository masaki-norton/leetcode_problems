# LeetCode Problems
This is my central knowledgebase for leetcode problems I have completed.\
The problems are following the outline provided by https://neetcode.io/roadmap

## Problems
### Arrays and Hashing
- 217 Contains Duplicate
- 242 Valid Anagram
- 1 Two Sum
- 49 Group Anagrams
- 347 Top K Frequemt Elements
- 238 Product of Array Except Self
- 36 Valid Sudoku
- 128 Longest Consecutive Sequence

### Two Pointers
- 167 Two Sum II
- 15 Three Sum
- 11 Container With Most Water
- 42 Trapping Rainwater

### Stack
- 20 Valid Parenthesis
- 155 Min Stack
- 150 Evaluate RPN
- 22 Generate Parentheses
- 739 Daily Temperatures
- 853 Car Fleet
- 84 Largest Rectangle in Histogram

### Binary Search
- 704 Binary Search
- 74 Search 2D Matrix
- 875 Koko Eating Bananas
- 153 Search Minimum in Sorted Array

### Other
- 1404 Number of Steps to Reduce Binary Number to 1


## Explanations and Key Points
### 217 Contains Duplicate
The runtime and memory of creating a set is the same as if it was written \
as a one liner comparing the lengths of the set and the original array.

### 242 Valid Anagram
One-liner is sorting both strings and comparing if they are equial. \
The other method is to create a dictionary of each letter occurrence and \
comparing the dictionaries.

### 1 Two Sum
Create a "subtracted" array, much faster than double loop.\
Check condition that return indices are not the same, and return.

### 49 Group Anagrams
Simple step of instructions:
1. Sort all words in list
2. Create dictionary where {key, value} = {index in nums, sorted word} \
and sort it by the values.
3. Loop through dictionary. If the values are the same, create sublist of anagrams\
to append to master output using dictionary keys. Repeat for all unique dictionary values.

### 347 Top K Frequent Elements
Simple step of instructions
1. Create letter counter
2. Sort counter dictionary based on values
3. Return top K values as a list

### 238 Product of Array Except Self
Each digit will be a product of both total products of its left and rigth side.\
Create two lists, each denoting all products on left side of index, and same for \
the right side. Multiply each list together to get the output.

### 36 Valid Sudoku
Brute force approach checking row, column, and 3x3 grid. \
Can possibly speed up by checking element-wise, potentially.

### 128 Longest Consecutive Sequence
Needs to be done in O(n) time. Approach is to create a set (remove duplicates) \
and for each number check if it is the start of a sequence, i.e., num-1 does not \
exist in the set. If it is the start of a sequence, enter while loop to continue \
checking if the next number is present. Note that sets can search in O(1) time, \
creating the benefit here.
Total passes are:
- one pass to create set
- another pass for outer for loop to check if each num is a sequence start
- and lastly counting each sequence is at worst o(n) if we visit all numbers once\
where there is no max sequence, and max sequence is 1.
The total time complexity is O(3n) ish.\

Another method is to create a set, and for each number, go up and down to count \
the sequence. This allows you to pop the number from the set, so it runs slightly \
faster.

### 125 Valid Palindrome
Straight forward, just check from either side.\
Dont forget the constraints - only alpha num and lower cases.

### 167 Two Sum II
Two pointers is one method to solve this problem.\
Go from left to right, shifting either left or right inward depending on the \
total sum compared to the target.\
Note that hash map is most likely faster, but two pointer uses very little memory.

### 15 Three Sum
Two pointer two sum, but start at each number in the array and loop thru.\
The tricky part about this was to not contain duplicates, so have to think \
thru the logic step by step on how to handle when seeing duplicates.\
The key was to recognize under which exact step would you want to perform the \
"skip this number because its a repeat" step within the loop.

### 11 Container With Most Water
Go from outside inwards. Logic here is that, in any given position, if the next \
bar is lower, it will hold less water (technically, the delta required for the \
height to next bar is anything greter than the width decrease by moving inward). \
Start with two pointers, left and right.\
Go inwards calculating area as necessary. Move inwards depending on which next \
bar is taller, and keep skipping over shorter next bars using while loops for \
a fast solution.

### 42 Trapping Rainwater (hard)
First approach was to go row by row. If there is blank space between blocks, \
it will hold water. Although this approach works, it times out, especially \
when the blocks are formatted in a way that is most time consuming with this \
algorithm. Tried tweaking the algorithm to drop the maximum amount (not row \
by row) however this did not give enough time savings.\
Next approach was to try two pointers. Start at left and right. If both pointers\
see a higher number (not just one, since a stick can't hold water), we \
check how much that gain was by and add it to the total rainwater.\
Another interesting method is to imagne sand being poured from the top, and \
to create a second array that only slopes downwards as it goes out.\
Given any arrangement of blocks, the shape is going to be "mound-like". \
Once you have this "mound-array", you would simply subtract the differences to \
see where blocks meet water, and therefore you have the total volume.\
The above worked, but it was way too slow. Refactored code so it runs faster.\

### 20 Valid Parenthesis
Straightforward stack implementation, no clever business.

### 155 Min Stack
Note that the class needs to retrieve min value of stack in O(1) time.\
Keep a second stack, updating the min values as elements move through the stack.

### 150 Evaluate RPM
Straight forward again, but just note that using int() will always tend towards zero.

### 22 Generate Parentheses
Use recursion and a stack.\
Important differences here is that we use stack.pop _after_ each recursion call\
to "revert" the stack back to its original form. This prevents having to pass the\
stack to the actual recursion.

### 739 Daily Temperatures
Use a stack of indices. This stack stores in only decreasing order, since \
we compare only against the top element. By making the stack decreasing, we can\
eliminate all cases like 71, 69,  74, 70, where although 70 is smaller than \
74, it is bigger than 69. But 69 won't be in the stack, since 74 already took\
care of it.

### 853 Car Fleet
This problem is a complicated way of comparing starting positions and ETAs.\
Given sorted starting positions from furthest away to the target, the only way\
a car "catches up" is if eta[i] is less than eta[i-1], if eta is a monotonically\
increasing stack. If the car catches up (stack[-1] <= eta), pop it off the stack.\
Repeat that process for all cars, and the length of the ETA stack is the number\
of fleets.

### 84 Largest Rectangle in Histogram
This is a two-part problem using a monotonically increasing stack.\
In the first part, when moving from left to right, we should check for a rectangle\
if the current number is smaller than the previous number, generally. To put it another\
way, calculating the rectangle for any given height is pointless if the next bar\
is higher, since it will always yield a larger rectangle. Therefore, we can eliminate\
those useless calculations by only calculating rectangles when we find that a number\
decreased as we move left to right. We create a stack, and pop items if they are\
larger than our current number. A few things we can say about the rectangle created\
by that popped number: 1) the rectangle's right side is always our current index - 1,\
since all elements to the right are highher than the popped index, and 2) the left \
side is the next index in the stack + 1, since all the indicies _above_ the next\
item down the stack are guaranteed to have at least the popped height (or else it\
would not have been added to the stack). With that, track and calculate max area\
as we move across the entire heights list.\

The second part to this problem is after we traverse the list, we can be left with \
a non-empty stack (this always happens if the last value != min(heights)). We need\
to cover potential rectangles created by the remaining elements in the stack.\
Similar to the above (but slightly different algo) to check heights possible with \
each index item. Key point is to consider carefully what we can assume about the boundaries\
of the rectangle created at our current bar's height.

### 704 Binary Search
Straightforward binary search. Alwayas be careful about the exit clause in the \
while loop, such that it will not break when l, m, r are close to eachother.

### 74 Search 2D Matrix
Two set of binary searches. First searches which array should be looked at,\
and the second searches if the target is in that array. Again, with any binary\
search, its important to know what the while loop escape mechanism is, and what\
exactly l,m,r would be when that loop exits.

### 875 Koko Eating Bananas
The search space is between 1 and the largest pile in the piles. Use a helper
method to determine if the eaating speed is quick enough, and throw out half
the search space accordingly. Note that, because an "equal" amount is acceptable,
i.e., if the bananaks are eaten as the guard arrives, this is considered possible,
our return case is >= instead of > in the helper method, and our loop runs from
l <= r not l < r. This puts us at the solutin where the helper method returns false,
so we return m + 1 for a guaranteed success.

### 153 Search Minimum in Sorted Array
Binary search is all about shrinking the search space by half the space at a time.
This problem is centered around sructuring the if else statements such that the
correct side of data is thrown out.

### 1404 Number of Steps to Reduce Binary Number to 1
Adding binary was easier converting it to an integer and reversing.\
Dividing by 2 in binary is simply shifting all digits over by 1, or \
discarding the last digit.
