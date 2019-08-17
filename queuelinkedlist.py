class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Queue:
    def __init__(self):
        self.head = None
    def enQueue(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            return
        p = self.head
        while p.link is not None:
            p = p.link
        p.link = temp
    def deQueue(self):
        if self.head == None:
            print("Queue is empty!")
            return
        self.head = self.head.link
    def display(self):
        if self.head == None:
            print("Queue is empty!")
            return
        p = self.head
        while p is not None:
            print(p.data," ",end = "")
            p = p.link
    def size(self):
        if self.head == None:
            return 0
        count = 0
        p = self.head
        while p is not None:
            count += 1
            p = p.link
        return count
    def peek(self):
        if self.head == None:
            print("Queue is empty!")
            return
        return self.head.data


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
            print("Size of Queue: ",qu.size())
        elif n == 5:
            print("Top of Queue: ", qu.peek())
        else:
            break
        
