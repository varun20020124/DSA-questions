class Solution:
    def characterReplacement(self, s, k):
        longest = 0
        i = 0 
        count = [0] * 26
        for j in range(len(s)):
            count[ord(s[j])-ord('A')]+=1
            if (j-i+1)-max(count)>k:
                count[ord(s[i])-ord('A')]-=1
                i+=1
            longest = max(longest, j-i+1)
        return longest
