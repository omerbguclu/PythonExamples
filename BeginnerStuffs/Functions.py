def hello():
    print("hello world")

hello()

def fill(a):
    print(a)

fill("meraba")
fill(54)

def fly(c):
    i=(c**2+100)/250
    if(i>120):
        print("its too much altitude")
        return
    else:
        print("you can fly at",i,"altitude")

fly(500)

def cat(height="nothing entered",weight="nothing entered"):
    print("your cat height is",height,"weight is", weight)

cat(12)
cat(weight=25)