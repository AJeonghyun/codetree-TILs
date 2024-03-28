arr = input().split()

cm = int(arr[0])
kg = int(arr[1])

b = (10000*kg) / (cm*cm)
b = int(b)
print(b)
if b>=25:
    print('Obesity')