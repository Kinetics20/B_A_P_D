#!/usr/bin/python3
# 

count = 0

while count < 30:
    count += 1
    if count == 14:
        break
    # if count %2 == 0:
    if count & 1 == 0:
        continue
    print("To sa liczby nieparzyste : {}".format(count))
    # if count %2 != 0:
    #     continue
    # print("To sa liczby parzyste : {}".format(count))


print('Koniec petli')