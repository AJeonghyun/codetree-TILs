def abc(y):
    if y%4==0:
        return 'true'
    if y%100==0 and y%400!=0:
        return 'false'
    else:
        return 'false'

n = int(input())
print(abc(n))