class Solution:
    def partition(self,s):
        def palindrome(string):
            return string == string[::-1]
        def backtrack(path,options):
            if len(options) == 0:
                result.append(path[:])
                return
            for i in range(1,len(options)+1):
                pre = options[:i]
                suf = options[i:]
                if not palindrome(pre):
                    continue
                path.append(pre)
                backtrack(path,suf)
                path.pop()
        result = []
        backtrack([],s)
        return result