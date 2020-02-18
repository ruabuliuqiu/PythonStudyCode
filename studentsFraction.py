#!usr/bin/env/ python3
#pan duan xue sheng cheng ji shi fou da biao 
#liufang 20200219
n = int(input("Enter the number of students: "))
data = {}                                      #yong lai cun chu shu ju de zi dian bian liang
Subjects = ('Physics', 'Math', 'History')          #Suo You Ke Mu
for i in range(0, n):
    name = input('Enter thr name of the student {}: '.format(i + 1))    #Huo De XueSheng Ming Zi
    marks = []                                     # marks shi ge liebiao
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x))))    #Huo De Mei Yi Ke De fenshu
    data[name] = marks                             # jiang xue sheng shu ju cun ru dao data zidian
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")

