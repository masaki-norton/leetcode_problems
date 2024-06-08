'''
https://leetcode.com/problems/search-a-2d-matrix/description/
'''

def searchMatrix(matrix: list[list[int]]) -> bool:
    return None

# test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3 # true

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13    # false

def main():
    print(searchMatrix(matrix1, target1))
    print(searchMatrix(matrix2, target2))
    return None

if __name__ == "__main__":
    main()
