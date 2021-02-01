class SumOfMul:
    
    def sum(self, mulNum):
        self.result = 0
        for n in range(1, 1000):
            if n % mulNum == 0:
                self.result += n
        return self.result
    
SOM  = SumOfMul()
som3 = SOM.sum(3)
som5 = SOM.sum(5)
som15 = SOM.sum(15)

print(som3 + som5 - som15)