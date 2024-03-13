"""
https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13
"""

def pivotInteger(n: int) -> int:
    if n == 1:
        return 1
    elif n == 0:
        return -1
    else:
        left_sum = int(n * (n + 1) / 2)
        right_sum = 0
        pivot = n
        while left_sum > right_sum:
            if left_sum == right_sum + pivot:
                return pivot
            left_sum -= pivot
            right_sum += pivot
            pivot -= 1
        return -1


# Test Cases
n1: int = 8
n2: int = 1
n3: int = 7

def main() -> None:
    print(f"{pivotInteger(n1) = }")
    # print(f"{pivotInteger(n2) = }")
    # print(f"{pivotInteger(n3) = }")

if __name__ == "__main__":
    main()
