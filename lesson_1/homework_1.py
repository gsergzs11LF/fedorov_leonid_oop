'''
++++++++++++++++++++++++++++++++++++++
Классы и атрибуты
++++++++++++++++++++++++++++++++++++++
'''

'''
1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
Проверь, как это повлияло на значения у обоих объектов.
Убедись, что __dict__ объектов отражает изменения.
'''
# class Dog:
#     species = "canis"
#     legs = 4
#
# akita_inu = Dog()
# woolf = Dog()
#
# akita_inu.species = 'Canis lupus familiaris'
# print(akita_inu.species) # - атрибут species был изменен
# print(woolf.species) # - атрибут species остался таким, какой был задан в классе Dog
# print(akita_inu.__dict__)
# print(woolf.__dict__)
# print(Dog.__dict__)

'''
2. Добавь в класс Dog строку документации, описывающую его назначение.
Затем выведи её на экран.
После этого добавь в объект класса новые атрибуты name и age,
а затем удали name.
Проверь, что произойдёт при попытке снова вывести объект.name.
'''
# class Dog:
#     "Класс для создания псовых животных"
#     species = "canis"
#     legs = 4
# print(Dog.__doc__) # - Выведет строку Класс для создания псовых животных
# akita_inu = Dog()
# akita_inu.name = 'Umi'
# akita_inu.age = 5
# print(akita_inu.__dict__)
# del akita_inu.name
# print(akita_inu.name) # - 'Dog' object has no attribute 'name'
# print(akita_inu.__dict__)

'''
3. Создай класс User с атрибутами класса role = "guest" и active = True.
С помощью функций getattr(), setattr(), hasattr() и delattr():

измени значение role на "admin",
проверь наличие active,
добавь новый атрибут email,
удали role.
Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
'''

# class User:
#     role = 'guest'
#     active = True
# setattr(User, 'role', 'admin') # - перезаписываем role на admin
# print('Новое значение аттрибута role:', getattr(User, 'role'))
# print('Есть ли атрибут active:', hasattr(User, 'active')) # - True
# setattr(User, 'email', 'sdf@sdf.sf')
# print('Новый атрибута email:', getattr(User, 'email'))
# delattr(User, 'role')
# print('Проверка удаления атрибута role:', getattr(User, 'role', 'атрибут не найден'))
# print(User.__dict__)