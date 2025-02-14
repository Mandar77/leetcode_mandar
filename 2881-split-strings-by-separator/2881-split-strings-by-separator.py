class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        result = []
        for word in words:
            split_result = word.split(separator)
            # Filter out empty strings
            result.extend(filter(None, split_result))
        return result
