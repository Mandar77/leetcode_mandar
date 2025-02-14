class Solution(object):
    def areNumbersAscending(self, s):
        s = s.split()
        numbers = []
        c = 0
        
        for i in range (len(s)):
            if s[i].isnumeric():
                numbers.append(int(s[i]))
        for i in range(1,len(numbers)):
            if (numbers[i]-numbers[i-1]<=c):
                return False
        return True
