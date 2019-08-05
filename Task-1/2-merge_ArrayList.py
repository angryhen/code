'''
python
'''
class Array:
    def __init__(self, cap=10, data=[]):
        self._len = len(data)
        self._cap = cap
        self._data = data+[None]*(self._cap-self._len)
        
    def make_new_array(self, new_cap):
        new_array = Array(new_cap)
        for i in range(self._len):
            new_array.add(i, self._data[i])
        self._cap = new_cap
        self._data = new_array._data
    
    def check_index(self, index):
        if index < 0 or index > self._len:
            raise Exception('Error index!')
        else:
            return index
        
    def add(self, index, elem):
        index = self.check_index(index)
        if self._len == self._cap:
            self.make_new_array(self._cap*2)
        for i in range(self._len-1, index-1, -1):
            self._data[i+1]=self._data[i]
        self._data[index] = elem
        self._len += 1
    
    def pop(self, elem):
        for i in range(self._len):
            if elem == self._data[i]:
                for j in range(i+1,self._len):
                    self._data[j-1] = self._data[j]
                self._len -= 1
                self._data[self._len] = None
                
    def change(self, index, elem):
        index = self.check_index(index)
        self._data[index] = elem
    
    def _print(self):
        print(self._data[:self._len])

def merge(a, b):
    c = Array()
    i, j = 0, 0
    index = 0
    while i<a._len and j<b._len:
        if a._data[i] <=b._data[j]:
            c.add(index, a._data[i])
            i += 1
        else:
            c.add(index, b._data[j])
            j += 1
        index += 1
    if i < a._len:
        for k in range(i, a._len):
            c.add(index, a._data[k])
            index += 1
    elif j < b._len:
        for k in range(j, b._len):
            c.add(index, b._data[k])
            index += 1   
    return c
    
if __name__ == '__main__':
    a = Array(data = [1,3,5,7,9])
    b = Array(data = [2,4,6,8,10,12])
    c = merge(a, b)
    c._print()
