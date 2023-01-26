#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.req=[]
    def countNum(self):
        for i in list(range(self.low, self.high+1)):
            if i%2 == 0:
                continue
            else:
                self.req.append(i)
        print(self.req)

        return len(self.req)
num=Solution(3,7)
print(num.countNum())


