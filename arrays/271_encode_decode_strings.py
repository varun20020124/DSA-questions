class Solution:
    def encode(self, strs):
        s = ""
        for string in strs:
            s+=str(len(string))+"#"+string
        return s
        
    def decode(self, s):
        strs = []
        i,j = 0,0
        while j<len(s):
            while s[i]!="#":
                i+=1
            length = int(s[j:i])
            j = i+1
            i = j+length
            strs.append(s[j:i])
            j = i
        return strs