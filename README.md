Отчёт по практической работе:  
После создания данный репозиторий был склонировал на пк с помощью команды - git clone https://github.com/theory-universe/home_practice_git.git.  
Следующим шагом было создание директории с окружением для расчётного скрипта .py и добавление её на основную ветку слежения main - git add calculating_the_triangle.  
Был создан коммит для этого шага - git commit -m "Add file .py 'Calculation the triangle'". Далее с помощью команды git push данная директория была добавлена на удалённый репозиторий.  

Сущность расчётного файла:  
  Вычисление площади треугольника в случае возможности его сущестования с вводными длинами сторон  
Скрипт:  
import math
a=(float(input('Введите сторону a: ')))  
b=(float(input('Введите сторону b: ')))  
c=(float(input('Введите сторону c: ')))  
if a<b+c and b<a+c and c<a+b:  
  corner_between_sides=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
  sin_corner = math.sin(math.radians(corner_between_sides))
  square_of_triangle=0.5*c*b*sin_corner
  print('Площадь треугольника: ', square_of_triangle)
else:
  print('Треугольник с данными сторонами не существует')

Далее была создана новая ветка и осуществлён переход на неё - git checkout -b feature_branch_counting_perimeter.
На новую ветку был добавлен новый скрипт .py с модификациями в проекте:

Изменения:
  Вычисление периметра в дополнение к вычислению площади
  Отрывок из скрипта с новым вычислением: print('Периметр треугольника: ', a+b+c)

Как и с основной веткой данный скрипт был доавбелн на удалённый репозиторий с коммитом:
git add calculating_the_triangle/calculating_the_triangle_perimeter.py
git commit -m "Add file .py 'Calculation the triangle's perimeter'"
git push -u origin feature_branch_counting_perimeter

Был создан pull-request в результате которого было одобрено слияние веток без изменений.
После проведения слияния на основной ветке располагается скрипт с возможностью вычисления периметра треугольника.


