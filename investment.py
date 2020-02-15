#!/usr/bin/env python3
#investment code
#liufang 20200215
amount = float(input("Enter amount: ")) #shu ru shu e
inrate = float(input("Enter Interest rate: ")) #shu ru li lv
period = int(input("Enter period: ")) #shu ru qi xian
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year += 1

