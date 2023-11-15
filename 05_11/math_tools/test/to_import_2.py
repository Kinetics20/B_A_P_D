# from ..math_tools.test.functions import quadratic_functions
#
# print(quadratic_functions(10, 5, 6, 8))

my_list = [1, 5, 8, 7, 9, 20, 50, 100]


def create_tuple(any_list):
    return (min(any_list), max(any_list))


print(create_tuple(my_list))
