# LeetCode Problems
This is my central knowledgebase for leetcode problems I have completed.\
The problems are following the outline provided by https://neetcode.io/roadmap

## Problems
### Arrays and Hashing
- 217 Contains Duplicate
- 242 Valid Anagram
- 1 Two Sum
- 49 Group Anagrams


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
