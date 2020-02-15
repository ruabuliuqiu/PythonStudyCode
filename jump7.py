#python test1 jump7 (1~100)
#liufang 20200215
for a in range(1,101):
    if (a%7 == 0) or (a%10 == 7) or (a/10 == 7):
        pass
    else:
        print(a)
