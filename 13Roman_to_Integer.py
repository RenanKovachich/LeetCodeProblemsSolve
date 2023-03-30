class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_values = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = prev_value = 0
        for i in range(len(s)-1, -1, -1):
            curr_value = roman_values[s[i]]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        return result
     