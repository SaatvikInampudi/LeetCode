class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for chars in zip(*strs):        # combines ith letters of all strings
            # print(chars)
            if len(set(chars)) == 1:    # all same letter
                res += chars[0]
                # print("h",chars)
            else:
                break
        return res