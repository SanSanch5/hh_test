import sys
import time
# from math import sqrt
# from itertools import count, islice

# def isPrime(n):
#     return all(n % i for i in islice(count(2), int(sqrt(n)-1)))

# q = 9100000
# while not isPrime(q):
#     q -= 1
# q = 100000004987
# print(q)
q = sys.maxsize // 10

class LongSequenceMaker:
    def __init__(self, findMe):
        assert findMe.isdigit() and int(findMe) > 0
        self.resizeFactor = 100000
        self.__curSequence = '1'
        self.__curNum = 1
        self.__pos = 1
        self.__localPos = 0
        self.__findMe = findMe
        num = len(findMe)
        self.__h = pow(10, num-1, q)
        self.__rang = num
        self.__t = self.__p = 0
        while len(self.__curSequence) < self.__rang:
            self.__curNum += 1
            self.__curSequence += str(self.__curNum)

    def next(self):
        fd = int(self.__curSequence[self.__localPos])
        if self.__localPos == self.resizeFactor:
            self.__localPos -= self.resizeFactor
            self.__curSequence = str(self.__curSequence)[self.resizeFactor:]
        if len(self.__curSequence) <= self.__localPos + self.__rang:
            # num = self.__curNum
            # for i in range(num,num + 10000):
            self.__curNum += 1
            self.__curSequence += str(self.__curNum)

        self.__localPos += 1
        self.__pos += 1
        self.__t = (10*(self.__t - fd * self.__h) + int(self.__curSequence[self.__localPos+self.__rang-1])) % q

    def count(self):
        for i in range(self.__rang):
            self.__p = (self.__p * 10 + int(self.__findMe[i])) % q
            self.__t = (self.__t * 10 + int(self.__curSequence[i])) % q

        while not (self.__p == self.__t and self.compare):
            self.next()
        return self.__pos

    @property
    def compare(self):
        cutted = str(self.__curSequence)[self.__localPos : self.__rang + self.__localPos]
        return cutted == self.__findMe


print("Input number: \n")
while True:
    seq = LongSequenceMaker(input())
    print(seq.count())
# for factor in range(1, 100, 10):
    # t = 0
    # for i in range(100):
    #     seq = LongSequenceMaker('756434')
    #     seq.resizeFactor = factor
    #     t1 = time.time()
    #     seq.count()
    #     t += time.time() - t1
    # print("\t{0} -".format(factor) + "\tTime elapsed: {:.3f}".format(t/100))