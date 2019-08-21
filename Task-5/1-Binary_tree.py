class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self, root=None):
        self.root = root

    # 添加节点
    def insert(self, elem):
        elem = Node(elem)
        if not self.root:
            self.root = elem
            return
        queue = [self.root]
        while True:
            tmp = queue.pop(0)
            if not tmp.left:
                tmp.left = elem
                return
            elif not tmp.right:
                tmp.right = elem
                return
            else:
                queue.append(tmp.left)
                queue.append(tmp.right)
                
    def search(self, cur, elem):
        if not cur:
            print('不存在')
            return False
        if elem == cur.data:
            print('存在')
            return cur
        if elem < cur.data:
            cur = cur.left
            self.search(cur, elem)
        else:
            cur = cur.right
            self.search(cur, elem)
            
    def delect(self, elem):
        tmp = self.search(self.root, root)
        if tmp == False:
            print('不存在')
            return          
        else:
            if tmp.left == None and tmp.right == None:
                pass

# 先序遍历
def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
    
a = BTree()
a.insert(5)
a.insert(2)
a.insert(7)
a.insert(1)
a.insert(3)
a.insert(6)
c = a.search(a.root, 5)
preorder(a.root)
inorder(a.root)
postorder(a.root)
