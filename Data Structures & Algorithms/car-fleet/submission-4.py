class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, v in zip(position, speed):
            cars.append([p, v])

        cars.sort(reverse=True)
        stack = []
        for car in cars:
            stack.append((target-car[0])/car[1])
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        