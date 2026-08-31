class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen={}
        l=r=0
        n=len(s)
        maxi=0
        while r<n:
            if s[r] not in seen:
                seen[s[r]]=r
                maxi=max(maxi,(r-l+1))
                r+=1
            else:
                if seen[s[r]]>=l:
                    l=seen[s[r]]+1
                seen[s[r]]=r
                maxi=max(maxi,r-l+1)
                r+=1
        return maxi




