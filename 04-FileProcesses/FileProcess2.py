with open("programmer.txt","r") as fileExample:
    fileExample.seek(10)
    print(fileExample.read())

    fileExample.seek(5)
    print(fileExample.read())

    fileExample.seek(5)
    print(fileExample.read(11))

