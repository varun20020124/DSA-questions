class Solution:
    def checkInclusion(self, s1, s2):
        def anagram(s,t):
            if len(s)!=len(t):
                return False
            count = [0]*26
            for i in range(len(s)):
                count[ord(s[i])-ord('a')]+=1
                count[ord(t[i])-ord('a')]-=1
            for num in count:
                if num != 0:
                    return False
            return True

        i,j = 0,len(s1)-1
        while j<len(s2):
            if anagram(s1,s2[i:j+1]):
                return True
            i+=1
            j+=1
        return False
            