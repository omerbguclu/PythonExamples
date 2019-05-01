a=True

while a:
    try:
        num1 = int(input("Enter a number:"))
        num2 = int(input("Enter a number:"))
        print(int(num1/num2))
        a=False
    except ValueError:
        print("Please enter a numbers")
    except ZeroDivisionError:
        print("Please enter different from zero for number 2")

try:
    file = open("pythonexamples.txt","r")
except IOError:
    print("File not found")
finally:
    file.close()