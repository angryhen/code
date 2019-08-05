```
python
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return
        
class SingleLink:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0 
        return
    def isEmpty(self):
        return (self.len == 0)
    
    def check_index(self, index):
        if self.isEmpty():
            raise Exception('SingleLink is Empty!')
        elif index < 0 or index > self.len:
            raise Exception('Error index!')
        else:
            return index
    
    def add_tail(self, elem):
        if not isinstance(elem, Node):
            elem = Node(elem)
        if not self.head:
            self.head = elem
        else:
            tmp_node = self.head
            while tmp_node.next:
                tmp_node = tmp_node.next
            tmp_node.next = elem
        self.len += 1
    
    def insert(self, index, elem):
        index = self.check_index(index)
        elem = Node(elem)
        tmp_node = self.head
        for i in range(self.len):
            if i == index-1:
                next_node = tmp_node.next
                tmp_node.next = elem
                elem.next = next_node
                self.len += 1
            tmp_node = tmp_node.next
        
    def delect(self, index):
        index = self.check_index(index)
        tmp_node = self.head
        count = 0
        pre = None
        while tmp_node:
            if index == count:
                if tmp_node == self.head:
                    self.head = tmp_node.next
                else:
                    pre.next= tmp_node.next
                break
            else:
                pre = tmp_node
                tmp_node = tmp_node.next
            count += 1
    
    def _print(self):
        p = []
        tmp_node = self.head
        while tmp_node:
            p.append(tmp_node.data)
            tmp_node = tmp_node.next
        print(p)

if __name__ == '__main__':
    a = SingleLink()
    a.add_tail(1)
    a.add_tail(2)
    a.add_tail('3')
    a.add_tail(4)
    a.add_tail('5')
    a.add_tail(6)
    a._print()
    a.delect(4)
    a._print()
    a.insert(4,5)
    a._print()
