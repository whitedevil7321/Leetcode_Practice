class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while (stack and asteroids[i]<0 and abs(asteroids[i])>stack[-1] and stack[-1]>0):
                stack.pop()
            if not stack:
                stack.append(asteroids[i])
            elif stack[-1]<0 or asteroids[i]>0:
                stack.append(asteroids[i])
            elif stack[-1]==abs(asteroids[i]):
                stack.pop()
        return stack
            
            
            