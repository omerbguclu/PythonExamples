dictionary = {"a":"1","b":"2","c":"3"}

print(dictionary["a"])

for i in dictionary.items():
    print(i)

for i in dictionary.items():
    print(i[0])
    print(i[1])

for i,j in dictionary.items():
    print("i",i,"j",j)
