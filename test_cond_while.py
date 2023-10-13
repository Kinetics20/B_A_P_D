#!/user/bin/python3
# 

wartosc = 0
while True:
    print("nieskonczonosc ")
    wartosc += 1
    if wartosc == 8:
        # exit()
        break
    elif wartosc %2 == 0:
        print("wartosci parzyste : {}".format(wartosc))
        continue
    elif wartosc %2 != 0:
        print("wartosci nieparzyste : {}".format(wartosc))
        continue