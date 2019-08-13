# 字典树
class Tri:
    def __init__(self):
        self.root = {}
        self.end = -1
        
    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur[self.end] = True
    def search(self, word):
        cur = self.root
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        if self.end not in cur:
            return False
        return True
   
if __name__ == '__main__':
    a = Tri()
    a.insert('hello')
    a.search('hell')
