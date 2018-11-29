#coding: utf-8
age = int(input('Пожалуйста укажите ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
    access = True  # доступ куда-либо
else:
    print('Доступ запрещен')
    access = False  # доступ куда-либо
