class Solution:
    def countAndSay(self, n: int) -> str:
        word = '11'
        if n == 1: return '1'
        if n == 2: return '11'
        for j in range(2,n):
            say = ''
            count = 1
            # print(word)
            for i in range(1,len(word)):
                # print(word)
                if word[i] == word[i-1]:
                    count += 1
                    # print(word)
                    if i == len(word) - 1:
                        say = say + str(count) + word[i-1]
                    # print(word)
                else: 
                    say = say + str(count) + word[i-1]
                    count = 1
                    # print(word)
                    if i == len(word) - 1:
                        say = say + str(count) + word[i]
                    # print(word)
            word = say
                
        return word



'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1' 
        if n == 2: return '11'
        elif n > 2:
            word = ''
            count = 1

        
            for i in range(1, len(self.countAndSay(n-1))):
                
                    
                if self.countAndSay(n-1)[i] == self.countAndSay(n-1)[i-1]:
                    count += 1
                    if i == len(self.countAndSay(n-1)) - 1:
                        word = word + str(count) + self.countAndSay(n-1)[i-1]
                else: 
                    word = word + str(count) + self.countAndSay(n-1)[i-1]
                    count = 1
                    if i == len(self.countAndSay(n-1)) - 1:
                        word = word + str(count) + self.countAndSay(n-1)[i]
                    # print(word)
            return word
'''



'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1' 
        if n == 2: return '11'
        # if n == 3: return '21'
        elif n > 2:
            if n == 3: return '21'
            
            for i in range(3,n+1):
                word = ''
                count = 1
                for j in range(1, len(self.countAndSay(i-1))):
                                
                    if self.countAndSay(i-1)[j] == self.countAndSay(i-1)[j-1]:
                        count += 1
                        if j == len(self.countAndSay(i-1)) - 1:
                            word = word + str(count) + self.countAndSay(i-1)[j-1]
                            # count = 1
                        # print(word)
                    else: 
                        word = word + str(count) + self.countAndSay(i-1)[j-1]
                        count = 1
                        # print(word)
                        if j == len(self.countAndSay(i-1)) - 1:
                            word = word + str(count) + self.countAndSay(i-1)[j]
                            # count = 1
                        # print(word)
            return word
'''