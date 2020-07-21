class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.values = []
    
    def add(self, number):
        # write your code here
        self.values.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        dic = {}
        for n in self.values:
            if n in dic:
                return True
            dic[value - n] = n
        return False
