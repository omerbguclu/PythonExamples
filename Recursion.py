def recursionfunc(a):
    a-=1
    print(a)
    if(a==0):
        return
    return recursionfunc(a)

print(recursionfunc(5))