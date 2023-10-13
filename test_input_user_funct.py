#!/usr/bin/python3

def shopping(section=[]):
    goods = len(section)
    basket = []
    watching_goods = 0
    while watching_goods < goods:
        print('\nYou are taking {} to your hands'.format(section[watching_goods]))
        decision = input('Would you like to add this product to your basket : ?')
        if decision == 'YES':
            basket.append(section[watching_goods])
            section[watching_goods] = ''
        watching_goods += 1
    return basket

def cash_registry(*argv):
    if argv is not None:
        for iarg in argv:
            for good in iarg:
                print(good, end=(', '))
    print('')

shop_shelf_1 = ['Apple' ,'Mandarine' ,'Nectarine' ,'Pineapple' ,'Pear' ,'Plum']
shop_shelf_2 = ['Toy_Train' ,'Toy_bear' ,'Toy_bicycle' ,'Toy_CAR' ,'Toy_Umbrella']

basket_1 = shopping(shop_shelf_1)
basket_2 = shopping(shop_shelf_2)
print('\n')
cash_registry(basket_1,basket_2)