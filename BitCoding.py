def shex(n):
    l = list()
    while n > 0:
        l.append(n % 64)
        n = n // 64
    l.reverse()
    s = ''
    for c in l:
        s += chr(c+32)
    return s

def xehs(s):
    n = ord(s[0])-32
    for c in s[1:]:
        n = n*64+(ord(c)-32)
    return n

def encode(txt):
    l = len(txt)
    s = {}
    for c in txt:
        if c in s:
            s[c] += 1
        else:
            s[c] = 1
    s = list(s.items())
    s.sort(key = lambda c: ord(c[0])+c[1]*100, reverse = True)
    res = ''
    bits = {}
    i = 0
    j = 1
    for c in s:
       res += c[0]
       bits[c[0]] = i
       i += 10**j
       j += 1
    n = ''
    m = ''
    for c in txt:
        n += str(bits[c])
    if len(n)//6 * 6 < len(n):
        n += '0' * ((len(n)//6+1) * 6 - len(n))
    for i in range(len(n)//6):
        m += chr(int(n[i*6:i*6+6],2)+32)
    return l,res, m


def decode(l,chars,code):
    bits = {}
    i = 0
    j = 1
    for c in chars:
       bits[c] = i
       i += 10**j
       j += 1
    res = ''
    for c in code:
        s = ''
        n = ord(c)-32
        m = n
        while n > 0:
            s = str(n%2) + s
            n = n//2
        if m < 32:
            if m < 16:
                s = '00' + s
            else:
                s = '0' + s
        if m == 0:
            s = '0'
        res += s
    res = res.split('0')
    res.pop()
    for i in range(len(res)):
        res[i] = res[i] + '0'
    s = ''
    for c in res:
        for k in list(bits.items()):
            if int(c) == k[1]:
                s+=k[0]
                break
    return s
                
            
    
