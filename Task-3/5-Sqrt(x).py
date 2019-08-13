class Solution:
    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x <= 1:
            return x
        # 起始的时候在 1 ，这可以比较随意设置
        cur = x/2
        while cur*cur > x:
            cur = (cur + x / cur) / 2
        return int(cur)
