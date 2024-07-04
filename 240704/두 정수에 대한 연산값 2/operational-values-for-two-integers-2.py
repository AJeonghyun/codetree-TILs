a,b = input().split(" ")
a = int(a)
b = int(b)



def abc(a,b):
    if a>b:
        b += 10
        a *= 2
        return a,b
    else:
        a += 10
        b *= 2
        return a,b

c,d = abc(a,b)

print(c, d)