# 数组实现队列

class Arr_queue:
    def __init__(self):
        self.data = []
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        return self.rear == self.front
    
    def en_queue(self, elem):
        self.data.append(elem)
        self.rear += 1
    
    def de_queue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print('空队列')
    
    def get_front(self):
        if not self.is_empty():
            return self.data[front]
        else:
            return
    
    def get_rear(self):
        if not self.is_empty():
            return self.data[rear-1]
        else:
            return 
        
# 链表实现队列

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Link_queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0
        
    def is_empty(self):
        return self.front == None
    
    def en_queue(self, elem):
        elem = Node(elem)
        if self.front == None:
            self.front = self.rear = elem
        else:
            self.rear.next = elem
            self.rear = elem
    
    def de_queue(self):
        if self.front == None:
            print('空栈')
        else:
            self.front = self.front.next
    
    def get_front(self):
        return self.front.data
    
    def get_rear(self):
        return self.rear.data
