#!/usr/bin/python3
def count_pln_eur(x , y):
    return x * y

def count_eur_pl(x , y):
    return x / y

print("Przelicznik walut : ")
print("1 - przelicz pln na eur")
print("2 - przelicz eur na pln")
print("3 - przelicz pln na usd")
print("4 - przelicz usd na pln")

choice = input("Wybierz przelicznik walut 1/2/3/4 : ")

if choice == "1":
    num_1 = float(input("Podaj ilosc pln : "))
    num_3 = float(input("Podaj kurs pln do eur : "))
    print("ilosc pln : " , num_1 , "ilosc eur to : " , count_eur_pl(num_1,num_3) )

elif choice == "2":
    num_2 = float(input("Podaj ilosc eur : "))
    num_3 = float(input("Podaj kurs eur do pln : "))
    print("ilosc eur : " , num_2 , "ilosc pln to : " , count_pln_eur(num_2,num_3) )

elif choice == "3":
    num_1 = float(input("Podaj ilosc pln : "))
    num_4 = float(input("Podaj kurs pln do usd : "))
    print("ilosc pln : " , num_1 , "ilosc usd to : " , count_pln_eur(num_1,num_4) )

elif choice == "4":
    num_5 = float(input("Podaj liczbe usd : "))
    num_4 = float(input("Podaj kurs usd do pln : "))
    print("ilosc usd : " , num_5 , "ilosc pln to : " , count_eur_pl(num_5,num_4) )

else:
    print("Nieporawna wartosc wyboru ")
