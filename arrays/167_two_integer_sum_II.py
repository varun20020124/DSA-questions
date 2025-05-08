class Solution:
    def twoSum(self, numbers, target):
        i,j = 0,len(numbers)-1
        while i<j:
            two_sum = numbers[i] + numbers[j]
            if two_sum < target:
                i+=1
            elif two_sum > target:
                j-=1
            else:
                return [i+1,j+1]
        return -1