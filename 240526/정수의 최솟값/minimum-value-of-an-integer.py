def abc(a,b,c):
    min_num = min(a,b,c)
    return min_num

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(abc(a,b,c))