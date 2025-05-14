class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        i,j = 0,0
        hashset = set()
        while j<len(s):
            if s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            else:
                hashset.add(s[j])
                j+=1
                longest = max(longest, j-i)
        return longest