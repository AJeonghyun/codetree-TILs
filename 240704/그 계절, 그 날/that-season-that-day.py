def day_test(year,month,day):
    if(year%4==0):
        yoon = 1
        if(year%100==0):
            yoon = 0
            if(year%400==0):
                yoon = 1
            else:
                yoon = 0
        else:
            yoon = 0
    else:
        yoon = 0
    
    if(yoon==1):
        if(1<=year<=3000) and (1<=month<=12) and (1<=day<=31):
            if(3<=month<=5):
                if(month==4 and day==31):
                    print(-1)
                else:
                    print("Spring")
            elif (6<=month<=8):
                if(month==6 and day==31):
                    print(-1)
                else:
                    print("Summer")
            elif (9<=month<=11):
                if(month==9 or month==11 and day==31):
                    print(-1)
                else:
                    print("Fall")
            else:
                if(month==2 and day>29):
                    print(-1)
                else:
                    print("Winter")
        else:
            print(-1)
    else:
        if(1<=year<=3000) and (1<=month<=12) and (1<=day<=31):
            if(3<=month<=5):
                if(month==4 and day==31):
                    print(-1)
                else:
                    print("Spring")
            elif (6<=month<=8):
                if(month==6 and day==31):
                    print(-1)
                else:
                    print("Summer")
            elif (9<=month<=11):
                if(month==9 or month==11 and day==31):
                    print(-1)
                else:
                    print("Fall")
            else:
                if(month==2 and day>28):
                    print(-1)
                else:
                    print("Winter")
        else:
            print(-1)

year,month,day = input().split(" ")
year = int(year)
month = int(month)
day = int(day)

day_test(year,month,day)