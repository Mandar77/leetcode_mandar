class Solution(object):
    def isAcronym(self, words, s):
        acronym = ''.join(word[0] for word in words)
        return acronym == s