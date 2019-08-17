class Queue:
    def __init__(self):
        self.list = []
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        return self.list.append(item)
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        ele = self.list[0]
        self.list = self.list[1:]
        return ele
    def display(self):
        print(self.list)
    def count(self):
        return len(self.list)
    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        return self.list[0]

if __name__ == "__main__":
    qu = Queue()
    while True:
        print("1.enQueue")
        print("2.deQueue")
        print("3.display")
        print("4.size")
        print("5.Top")
        print("6.Quit")

        n = int(input("Enter your choice:"))

        if n == 1:
            item = int(input("Enter element:"))
            qu.enQueue(item)
        elif n == 2:
            qu.deQueue()
        elif n == 3:
            qu.display()
        elif n == 4:
            print("Size of Queue: ",qu.count())
        elif n == 5:
            print("Top of Queue: ", qu.peek())
        else:
            break
