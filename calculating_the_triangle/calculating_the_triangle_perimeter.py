import math
a=(float(input('Введите сторону a: ')))
b=(float(input('Введите сторону b: ')))
c=(float(input('Введите сторону c: ')))
if a<b+c and b<a+c and c<a+b:
  corner_between_sides=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
  sin_corner = math.sin(math.radians(corner_between_sides))
  square_of_triangle=0.5*c*b*sin_corner
  print('Площадь треугольника: ', square_of_triangle)
  print('Периметр треугольника: ', a+b+c)
else:
  print('Треугольник с данными сторонами не существует')
