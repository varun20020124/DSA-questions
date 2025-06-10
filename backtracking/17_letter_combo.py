class Solution:
    def letterCombinations(self, digits):
        def backtrack(path,options):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            i = len(path) 
            for char in hashmap[options[i]]:
                path.append(char)
                backtrack(path,options)
                path.pop()
        hashmap = {"2" : "abc", "3" : "def", "4" : "ghi", 
                "5" : "jkl", "6" : "mno", "7" : "pqrs",
                "8" : "tuv", "9" : "wxyz"}
        if not digits:
            return []
        result = []
        backtrack([],digits)
        return result