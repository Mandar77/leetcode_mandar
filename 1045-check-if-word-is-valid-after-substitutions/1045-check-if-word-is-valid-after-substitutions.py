class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for char in s:
            if char == 'c':
                if len(stk)>=2 and stk[-1] == 'b' and stk[-2] == 'a':
                    stk.pop()
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)
        return not stk        