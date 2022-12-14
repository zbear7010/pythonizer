'''

Вариант с позиционным подходом к назначению переменных и выводом с помощью метода f-строк.
Такой упрощенный способ метода \".format\". Чистый и кристально ясный.

'''

# Тут для передачи значений в переменные применен метод ПОЗИЦИОННОГО ПРИСВАИВАНИЯ. В две строки — для наглядности.
index, city, street, house, flat = 443322, "Москва", "Ленина пр-т", "д. 7", "кв. 1"
lastname, firstname, patronymic = "Иванов", "Иван", "Иванович"

# С помощью f-строк (f''), можно сократить довольно большие конструкции и тоже повысить наглядность.
print(f'\nКуда: {index}, г. {city}, {street}, {house}, {flat}.\nКому: {lastname} {firstname} {patronymic}.')

'''

Куда: 443322, г. Москва, Ленина пр-т, д. 7, кв. 1.
Кому: Иванов Иван Иванович.

[Finished in 169ms]

'''