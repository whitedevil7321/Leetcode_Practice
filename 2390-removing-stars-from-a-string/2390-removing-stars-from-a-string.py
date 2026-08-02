from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack=deque()
        for ch in s:
            if ch=="*" and stack:
                stack.pop()
            else:
                stack.append(ch)
        ans=[]
        while stack:
            ans.append(stack.popleft())
        return "".join(ans)