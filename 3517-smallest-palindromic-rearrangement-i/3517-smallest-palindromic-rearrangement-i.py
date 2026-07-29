
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        right=""
        freq=[0]*26
        mid_ele=s[len(s)//2] if len(s)%2==1 else ""
        for ch in range(len(s[:len(s)//2])):
            freq[ord(s[ch])-97]+=1
        for i in range(26):
            right+=(chr(i+97)*freq[i])
        return ""+(right+mid_ele+right[::-1])
            






        