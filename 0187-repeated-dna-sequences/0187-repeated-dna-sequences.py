class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []

        sequences = defaultdict(int)
        result = []

        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequences[sequence] += 1

        for seq, count in sequences.items():
            if count > 1:
                result.append(seq)

        return result