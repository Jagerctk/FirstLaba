# TODO Найдите количество книг, которое можно разместить на дискете
a = 1.44 # объем дискеты в Мб
b = a*1024*1024 # объем в байтах
c = 4*25*50*100 # Занимает одна книга
d = b//c
print("Количество книг, помещающихся на дискету:", round(d,))
