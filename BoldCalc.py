def BoldCalc():
    global s, txt
    for s in txt:
        try:
            print(eval(s, locals()))
        except:
            try:
                exec(s, locals())
            except SyntaxError as SE:
                if '=' in s:
                    print("invalid identifier '" + s.split('=')[0] +"'")
                else:
                    print(SE)
            except NameError as NE:
                if '=' in s:
                    print("invalid assignment '" + s +"'")
                else:
                    print(NE)
            except BaseException as EXC1:
                    print(EXC1)
txt = list() 
s = input()
while s not in {'.', ''}:
    if s[0] != '#':
        txt.append(s)
    s = input()
BoldCalc()

        
