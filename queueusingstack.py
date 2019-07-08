class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,data):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(data)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

        print("%d appended"%data)

    def deQueue(self):
        if len(self.s1) == 0:
            print("Q is Empty")

        x = self.s1[-1]
        self.s1.pop()
        return x

ob = Queue()
ob.enQueue(12)
ob.enQueue(17)
print(ob.deQueue())
