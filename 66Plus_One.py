class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        number = int("".join(s))
        number = int(number) + 1
        return list(map(int, str(number)))