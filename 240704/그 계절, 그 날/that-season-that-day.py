year,month,day = input().split(" ")
year = int(year)
month = int(month)
day = int(day)



if (1<=year<=3000) and (1<=month<=12):
    if(year%4==0):
        if(year%100==0 and year%400==0):
            if(30<=day<=31):
                print(-1)

        if(3<=month<=5):
            print("Spring")
        elif (6<=month<=8):
            print("Summer")
        elif (9<=month<=11):
            print("Fall")
        else:
            print("Winter")
else :
    print(-1)