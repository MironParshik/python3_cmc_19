a = input()
s1 = set(a)
s2 = set()
flag = False
b = input()
while b != "":
    if flag:
        s1 = s1|set(b)
        flag = False
    else:
        s2 = s2|set(b)
        flag = True
    b = input()
if len(s1) > len(s2):
    s1name = "Mumbo"
    s2name = "Jumbo"
else:
    s1name = "Jumbo"
    s2name = "Mumbo"
if s1.issuperset(a):
    print(s1name)
else:
    print(s2name)
