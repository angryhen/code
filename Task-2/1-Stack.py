
# 数组实现顺序栈
class Arr_stack:
    def __init__(self):
        self.data = []
    def is_empty(self):
        return (len(self.data) == 0)
    def push(self,elem):
        self.data.append(elem)
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return 
    def top(self):
        if not self.is_empty():
            return self.data[len(self.data)-1]
        else:
            print('空栈')
            return

# 链表实现顺序栈
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Link_stack:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def isEmpty(self):
        return (self.len == 0) 
    
    def push(self, elem):
        p = Node(elem)
        p.next = self.head
        self.head = p
        self.len += 1
    
    def pop(self):
        tmp = self.head
        if tmp != None:
            self.head = tmp.next
            self.len -= 1
        else:
            print('空栈')
        
    def top(self):
        if self.head != None:
            return self.head.data
        else:
            print('空栈')
