class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        last_word = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            last_word = s[i] + last_word
        return len(last_word)