class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        beg = 0

        result = 0
        char_dict = {}

        for i in range(len(s)):
            char = s[i]

            exist_ind = char_dict.get(char, -1)
            if exist_ind >= beg:
                beg = exist_ind + 1

            char_dict[char] = i
            cur_len = i - beg + 1

            if cur_len > result:
                result = cur_len

        return result
