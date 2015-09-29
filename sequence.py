class LongSequenceMaker:
    def __init__(self, findMe):
        assert findMe.isdigit and int(findMe) > 0
        self.__curSequence = '1'
        self.__curNum = 1
        self.__pos = 1
        self.__findMe = findMe
        num = len(findMe)
        self.__rang = num
        while len(self.__curSequence) < num:
            self.__curNum += 1
            self.__curSequence += str(self.__curNum)

    def next(self):
        self.__curSequence = str(self.__curSequence)[1:]
        self.__pos += 1
        if len(self.__curSequence) < self.__rang:
            self.__curNum += 1
            self.__curSequence += str(self.__curNum)

    def count(self):
        while not self.compare:
            self.next()
        return self.__pos
            
    @property
    def compare(self):
        cutted = str(self.__curSequence)[:self.__rang]
        return cutted == self.__findMe

print("Input number:\n")
while True:
    seq = LongSequenceMaker(input())
    print("\t" + str(seq.count()))