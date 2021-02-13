# 2021 Jan Amazon OA
# each time the direction change range is between 0 to 3, so 4 times later must come back to same direction
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if not instructions:
            return True
        # n: 0, e: 1, s: 2, w: 3
        state = { 0: 0, 1: 0, 2: 0, 3: 0 }
        direction = 0
        turns = 1
        while turns <= 4:
            for c in instructions:
                if c == 'G':
                    state[direction] += 1
                if c == 'L':
                    direction = (direction + 3) % 4
                if c == 'R':
                    direction = (direction + 1) % 4
            if state[0] == state[2] and state[1] == state[3]:
                return True
            turns += 1
        return False
