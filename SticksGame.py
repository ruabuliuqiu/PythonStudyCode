#This is a sticks game
#liufang 20200216
sticks = 21

print("There are 21 sticks, you can take 1~4 number of sticks at a time.")
print("Whoever will take the last sticks will loose")

while True:
    print("Sticks left:{} ".format(sticks))
    if sticks == 1:
        print("You took the last sticks, you loose")
        break
    sticks_taken = int(input("Take sticks(1~4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took:{} ".format(5 - sticks_taken))
    sticks -= 5
