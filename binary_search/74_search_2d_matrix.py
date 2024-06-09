'''
https://leetcode.com/problems/search-a-2d-matrix/description/
'''

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    b, t = 0, len(matrix) - 1
    m = (t + b) // 2

    while b < t:
        if matrix[m][0] == target:
            return True
        elif matrix[m][-1] < target:
            b = m + 1
            m = (t + b) // 2
        else:
            t = m
            m = (t + b) // 2

    inner_list = matrix[m]
    l, r = 0, len(inner_list) - 1
    m = (l + r) // 2
    while l <= r:
        if inner_list[m] == target:
            return True
        elif inner_list[m] < target:
            l = m + 1
            m = (l + r ) // 2
        else:
            r = m - 1
            m = (l + r ) // 2

    return False

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
