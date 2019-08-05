'''
python-ArrayList
'''
class Array:
    def __init__(self, cap=10, data=[1]):
        self._len = len(data)
        self._cap = cap
        self._data = data+[None]*(self._cap-self._len)
        
    def make_new_array(self, new_cap):
        new_array = Array(new_cap)
        for i in range(self._len):
            new_array.add(i, self._data[i])
        self._cap = new_cap
        self._data = new_array._datata
    
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
        
if __name__ == '__main__':
    a = Array(data = [1,2,3,4,5])
    # 打印
    a._print()1
