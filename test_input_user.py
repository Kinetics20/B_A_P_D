#!/usr/bin/python3
# sth

shop_shelf = ['Brush' ,'Soft toy' ,'Banna' ,'orange' ,'Apple']

basket = []

goods = len(shop_shelf) - 1

print('in our shop we have : ')
for assortments in shop_shelf:
    print(assortments , end=(', '))

watching_goods = 0
while watching_goods <= goods:
    print('\nYou are taking {} to your hand '.format(shop_shelf[watching_goods]))
    decision = input('Would you like to add this product to your basket / YES or NO / : ')
    if decision == 'YES':
        basket.append(shop_shelf[watching_goods])
        shop_shelf[watching_goods] = ''
    watching_goods += 1

print('\nYou have in your basket : ')
for in_basket in basket:
    print(in_basket, end=', ')
print('\n')
print('\nIn our shop left : ')
for assortments in shop_shelf:
    print(assortments, end=', ')