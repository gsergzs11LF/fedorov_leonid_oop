class Animal: # - сам класс
    color = 'green' # - атрибут класса (или свойства класса)
    paws = 4 # - атрибут класса

Animal.paws = 2 # - изменяем атрибут самого класса
print('Paws:', Animal.paws) # - выводим атрибут класса выведет 2, так как поменяли у самого класса

cat = Animal() # - создали отдельный объект класса
cat.paws = 4 # -изменили атрибут у ОБЪЕКТА класса
print('Paws cat:', cat.paws) # - выводим атрибут объекта класса. Выведет 4, так как поменяли именно у объекта класса
print('Color cat:', cat.color)

dog = Animal()
dog.color = 'white'
print('Paws dog:', dog.paws)
print('Color dog:', dog.color)




# print('All attr:', Animal.__dict__ ) # - выводим ВСЕ атрибуты класса (или свойства класса)

