def abc(a,b):
    num = 0
    sum_num = 0
    for i in range(a,b+1):
        for j in range(1,i+1):
            if(i%j==0):
                num+=1
        if(num==2):
            sum_num += i
        num = 0
    return sum_num

a,b = input().split()
a = int(a)
b = int(b)

print(abc(a,b))