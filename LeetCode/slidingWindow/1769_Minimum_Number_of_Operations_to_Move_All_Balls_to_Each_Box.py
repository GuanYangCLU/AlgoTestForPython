class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_one = 0
        right_one = sum([int(c) for c in boxes])
        val = sum([ idx * int(boxes[idx]) for idx in range(len(boxes)) ])
        res = [val]
        for i in range(len(boxes) - 1):
            left_one += int(boxes[i])
            right_one -= int(boxes[i])
            val = val + left_one - right_one
            res.append(val)
        return res
        
