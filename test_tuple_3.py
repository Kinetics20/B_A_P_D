#!/user/bin/python3

my_list = [8 ,9 ,10 ,33]
my_list[3:] = [800 ,900 ,700]
my_tuple = tuple(my_list)
print('values in tuple : {} | object type is {}'.format(my_tuple,type(my_tuple)))
print('\aamount of values in tuple : {}\nmin value in tuple is : {}\nmax value in tuple is : {}\nsum of all values in tuple is : {}'.format(len(my_tuple),min(my_tuple),max(my_tuple),sum(my_tuple)))
for v in my_tuple:
    # print('\n')
    print(v, end=', ')

# kkk = my_tuple[0]
# print(type(kkk))
print('\n')
a,b,c,d,e,f = my_tuple
print(a,b,c,d,e,f)
my_tuple_new = my_tuple + (1000,3000,6000)
for nn in my_tuple_new:
    print(nn, end=', ')