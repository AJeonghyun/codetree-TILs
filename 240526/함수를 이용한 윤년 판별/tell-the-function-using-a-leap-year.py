def abc(y):
    if y%4==0:
        if y%100==0 and y%400!=0:
            return 'false'
        else:
            return 'true'
    else:
        return 'true'

n = int(input())
print(abc(n))