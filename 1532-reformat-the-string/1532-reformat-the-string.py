class Solution(object):
    def reformat(self, s):
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []
        # Interleave the letters and digits
        if len(letters) >= len(digits):
            for letter, digit in zip(letters, digits):
                result.extend([letter, digit])
            if len(letters) > len(digits):
                result.append(letters[-1])
        else:
            for letter, digit in zip(letters, digits):
                result.extend([digit, letter])
            result.append(digits[-1])

        return ''.join(result)