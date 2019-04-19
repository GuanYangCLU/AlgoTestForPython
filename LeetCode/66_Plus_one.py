class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return [int(j) for j in list(str(int(''.join([str(i) for i in digits])) + 1))]
        plus = 1
        i = len(digits) - 1
        while i > -1:
            if plus == 1:
                digits[i] += 1
                if digits[i] > 9:
                    digits[i] = digits[i]%10
                    if i == 0:
                        digits = [1] + digits
                else: plus = 0
            i -= 1
                
        return digits