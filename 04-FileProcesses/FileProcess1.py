try :
    fileExample=open("programmer1.txt","r")
except FileNotFoundError:
    print("file not found")

fileExample = open("programmer.txt","r")

print("all file printed\n",fileExample.read(),"\n")
fileExample.close()

fileExample = open("programmer.txt","r")
print("first line printed\n",fileExample.readline(),"\n")


fileExample.close()