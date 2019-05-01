with open("programmer.txt","r+") as fileExample:
    list = fileExample.readlines()
    list.insert(1,"Its a breakline\n")
    fileExample.seek(0)
    fileExample.writelines(list)

with open("programmer.txt","r+") as fileExample:
    data = fileExample.read()
    data = "its a starting\n" + data
    fileExample.seek(0)
    fileExample.writelines(data)