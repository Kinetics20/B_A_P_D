#!/usr/bin/python3

def find_boundaries(any_list):
    new_list = []

    for value in any_list:
        if isinstance(value, (int, float)):
            new_list.append(value)
    if not any_list:
        return None

    return (min(new_list), max(new_list))


m_list = [1, 2, 3.14, 3, 42]
m_list_2 = []
m_list_3 = [-1, 2, 3.14, 3, 80, 'Home', 'Theatre', 'Oracle']

print(find_boundaries(m_list))
print(find_boundaries(m_list_2))
print(find_boundaries(m_list_3))


def find_boundaries_2(any_list):
    if not any_list:
        return
    new_list = [value for value in any_list if isinstance(value, (int, float))]

    return min(new_list), max(new_list)


m_list = [1, 2, 3.14, 3, 42]
m_list_2 = []
m_list_3 = [-1, 2, 3.14, 3, 80, 'Home', 'Theatre', 'Oracle']

print(find_boundaries_2(m_list))
print(find_boundaries_2(m_list_2))
print(find_boundaries_2(m_list_3))
