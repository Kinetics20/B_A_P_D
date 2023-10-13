#!/user/bin/python3

point = ( 2.0 , 3.0)
point_3d = point + (4.6,)
print(point_3d,type(point_3d))
for v in point_3d:
    # print('\n')
    print(v , end=', ')
point_4d = point + (5.7,6.8,9.7)
print(point_4d,type(point_4d))
for d in point_4d:
    print(d, end=', ')