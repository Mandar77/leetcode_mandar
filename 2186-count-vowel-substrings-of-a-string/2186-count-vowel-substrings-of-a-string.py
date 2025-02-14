class Solution(object):
    def vowel(self,word):
        v = defaultdict(int)
        for i in word:
            if i not in {"a","e","i","o","u"}:
                return False
            else:
                v[i]+=1
        return all (v[i]>=1 for i in {"a","e","i","o","u"})
    def countVowelSubstrings(self, word):
        n = len (word)
        
        if n<5:
            return 0
        
        ans = 0
        for i in range (n):
            for j in range (i+4,n):
                w=word[i:j+1]
                if self.vowel(w):
                    ans+=1
        
        return ans


        