inp=input("enter password")
inp=str(inp)
a=len(inp)
count=0
if a>=6 and a<=12:
    for i in range (a):
        if inp[i].isdigit:
            count=count+1
    if count<0:
        print("wrong input")
    else:
        print("verified")
else:
    print("wrong input")
