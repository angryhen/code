def match(s, t):
    i = j = 0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == len(t):
        return True
    else:
        return False
    
if __name__ == '__main__':
    match('absfasf','absa')
