s = input()
a = input()
b = a.split('@')
n1 = s.find(b[0])
l = len(b[0])
if l == 0:
    l += 1
while n1 != -1:
    flag = True
    n2 = n1
    for i in range(1,len(b)):
        if b[i] == s[n2+len(b[i-1])+1:n2+len(b[i-1])+1+len(b[i])]:
            n2 = n2+len(b[i-1])+1
        else:
            n1 = s.find(b[0], n1+l)
            flag = False
            break
    if flag:
        break
print(n1)
            
    
    
