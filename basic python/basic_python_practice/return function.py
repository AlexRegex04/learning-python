def add(a,b):
    if a>0 and b>0 and a<=100 and b<=100:
        add = a+b
        return print("add:"+str(add)+"and "+str(a)+","+str(b)+"<=100")                                                                                                                                                                   
    elif a<0 and b<0:
        add = a+b
        return print("add:"+str(add)+"and "+str(a)+","+str(b)+"nagetive number")
    else:
        return print("add:"+str(a+b)+"and "+str(a)+","+str(b)+"huge number")
x = add(int(input('parameter(a)')),int(input('parameter(a)')))