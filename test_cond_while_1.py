#!/usr/bin/python3
# 

count = 0
while count < 30:
    count += 1
    if count %2 == 0:
        continue # pomija warunek i przechodz dalej , czyli pomija parzysta i przechodzi
    # dalej gdzie jest drukowanie nastepnej wartosci , a nastepna jest nieparzysta
    if count %20 == 0:
        break 
    print("liczby nieparzyste : {}".format(count))
    count += 1

print('Koniec petli')