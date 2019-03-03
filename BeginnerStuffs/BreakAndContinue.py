a=5

for i in range(10):
    print("i nin değeri:",i,"   a nın değeri:",a)
    if(i>a):
        print("it breaked")
        break


b=5

for i in range(10):
    if(i>b):
        print("it passed one")
        continue
    print("i nin değeri:",i,"   b nın değeri:",b)


