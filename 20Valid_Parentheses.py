class Solution:
    def isValid(self, s: str) -> bool:
        sirs = []
        characters = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in characters:
                top_element = sirs.pop() if sirs else '#'
                if characters[char] != top_element:
                    return False
            else:
                sirs.append(char)
        return not sirs
    