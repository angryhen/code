class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        l = []
        for i in s:
            if i in d:
                tmp = l.pop() if l else '#'
                if d[i] != tmp:
                    return False
            else:
                l.append(i)
        return not l
