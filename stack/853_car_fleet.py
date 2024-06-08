'''
https://leetcode.com/problems/car-fleet/description/
'''

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # use a mononotic stack of cars with decreasing ETA and return the len(stack)
    stack = []
    cars = sorted(list(zip(position, speed)), key=lambda x: x[0])
    for i, car in enumerate(cars):
        eta = (target - car[0]) / car[1]
        while stack and stack[-1] <= eta:
            stack.pop()
        stack.append(eta)
    return len(stack)

# test cases
target1 = 10
position1 = [3]
speed1 = [3]    # 1

target2 = 100
position2 = [0,2,4]
speed2 = [4,2,1]    # 1

target3 = 12
position3 = [10,8,0,5,3]
speed3 = [2,4,1,1,3]    # 3

def main():
    print(carFleet(target1, position1, speed1))
    print(carFleet(target2, position2, speed2))
    print(carFleet(target3, position3, speed3))
    return None

if __name__ == "__main__":
    main()
