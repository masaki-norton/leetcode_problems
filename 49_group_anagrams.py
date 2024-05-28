'''
https://leetcode.com/problems/group-anagrams/
'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    sorted_words = []
    for word in strs:
        sorted_words.append("".join(sorted(word)))
    word_dict = {}
    for x in range(len(strs)):
        word_dict[x] = sorted_words[x]
    sorted_dict = dict(sorted(word_dict.items(), key=lambda x: x[1]))
    output = []
    to_add = []
    c = 0
    for key in sorted_dict.keys():
        if to_add == []:
            to_add.append(strs[key])
            c += 1
        elif sorted_dict[key] == "".join(sorted(to_add[0])):
            to_add.append(strs[key])
            c += 1
        else:
            output.append(to_add)
            to_add = []
            to_add.append(strs[key])
            c += 1
        if c == len(strs):
            output.append(to_add)
    return output

# test cases
strs1 = ["eat","tea","tan","ate","nat","bat"]   # [["bat"],["nat","tan"],["ate","eat","tea"]]
strs2 = [""]    # [[""]]
strs3 = ["a"]   # [["a"]]

def main():
    print(f'{groupAnagrams(strs1) = }')
    print(f'{groupAnagrams(strs2) = }')
    print(f'{groupAnagrams(strs3) = }')

if __name__ == "__main__":
    main()
