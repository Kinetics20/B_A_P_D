#!/user/bin/python3
# List in python

my_list = [332 , 144 , 444 ]
my_list.append(20)
print(my_list)
my_index = len(my_list) - 1
print("Ostatni index z my_list to : {} ".format(my_list[my_index]))
print("cala lista : {} typ : {}".format(my_list,type(my_list)))
print("ilosc index-ow w liscie : {}".format(my_index))
print("index 0 : {} index 1 : {} index 2 : {} index 3 : {}".format(my_list[0],my_list[1],my_list[2],my_list[3]))
my_list[2]=100
my_list[3]=500
my_list.append(490)
my_list.append(1200)
print("index 3 : {}".format(my_list[3]))
print("cala lista : {}".format(my_list))
my_list.remove(1200)
my_list[4] = "Hate"
print("cala lista : {}".format(my_list))
my_list.pop()
my_list.pop()
print("cala lista : {}".format(my_list))
my_list[1:2] = ["world" , 3 , "where" , 5]
print("cala lista : {}".format(my_list))
my_list[2:5]=[]
print("cala lista : {}".format(my_list))
my_list.append(500)
my_list.append('zigzak_gosh')
my_list.append("tttt_ttttt")
print("cala lista : {}".format(my_list))
my_list.pop(2)
print("cala lista : {}".format(my_list))
my_list[5:] = [100 , 30 , 40 , 50 , 677 , "god please help me"]
print("cala lista : {}".format(my_list))
my_list.remove("god please help me")
print("cala lista : {}".format(my_list))
my_list.remove(100)
print("cala lista : {}".format(my_list))
my_list[:5]=[]
print("cala lista : {}".format(my_list))
my_list_2 = ['mouse','whole', 'big', 40 , 340]
my_list += my_list_2
print("a loto cala lista : {}".format(my_list))