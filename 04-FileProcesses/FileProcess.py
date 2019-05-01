fileExample = open("programmer.txt","w")

fileExample.write("Best programming language is java")

fileExample = open("programmer.txt","a")

fileExample.write(" also Ruby\n")
fileExample.write("hey")

fileExample.close()