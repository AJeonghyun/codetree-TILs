def dfg(n):
    while n>0:
        if n%10==3 or n%10==6 or n%10==9:
            return True
        n //= 10


def abc(a,b):
    sum_num = 0
    for i in range(a,b+1):
        if (dfg(i) or i%3==0):
            sum_num+=1
    return sum_num


a,b = input().split()
a = int(a)
b = int(b)

print(abc(a,b))