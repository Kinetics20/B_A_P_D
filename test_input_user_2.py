#!/usr/bin/python3

shop_shelf = ['Roof tail' ,'Apple' ,'Pear' ,'Apple' ,'Door mat']

basket = []

goods = len(shop_shelf) - 1

print('')
print('We have in our shop : ')
for assortments in shop_shelf:
    print(assortments, end=', ')

watching_goods = 0
while watching_goods <= goods:
    print('\nYou took {} to your hand : '.format(shop_shelf[watching_goods]))
    decision = input('Would you like to add it to your basket ? ')
    if decision == 'YES':
        basket.append(shop_shelf[watching_goods])
        shop_shelf[watching_goods] = ''
    watching_goods += 1

print('\nYou have in your basket : ')
for in_basket in basket:
    print(in_basket ,end=', ')
print('\n')
print('\nIn our shop left : ')
for assortments in shop_shelf:
    print(assortments ,end=', ')