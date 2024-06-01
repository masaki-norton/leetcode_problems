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
Two pointers is one method to solve this problem.\
Go from left to right, shifting either left or right inward depending on the \
total sum compared to the target.\
Note that hash map is most likely faster, but two pointer uses very little memory.

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

### 1404 Number of Steps to Reduce Binary Number to 1
Adding binary was easier converting it to an integer and reversing.\
Dividing by 2 in binary is simply shifting all digits over by 1, or \
discarding the last digit.
