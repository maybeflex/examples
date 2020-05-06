import FNC

head = tail = None
head, tail = FNC.add_to_back(10, head, tail)
head, tail = FNC.add_to_back(20, head, tail)
head, tail = FNC.add_to_back(30, head, tail)
head, tail = FNC.add_to_front(5, head, tail)
head, tail = FNC.add_to_back(40, head, tail)

print('Наполнили список элементами')
print('Голова и хвост:')
print(head, tail, end='\n\n')

print('Элементы друг за другом:')
print(FNC.print_one_by_one(head, tail), end='\n\n')

print('Поиск элемента со значением 20:')  # такой элемент в списке есть
print(FNC.search(20, head, tail), end='\n\n')

print('Поиск элемента со значением 100:')  # этого элемента в списке нет, выводит ошибку, но не ломается
print(FNC.search(100, head, tail), end='\n\n')

print('Поиск элемента с индексом 0:')  # такой элемент в списке есть
print(FNC.get_by_index_1(0, head, tail), end='\n\n')

print('Поиск элемента с индексом 6:')  # этого элемента в списке нет, выводит ошибку, но не ломается
print(FNC.get_by_index_1(4, head, tail), end='\n\n')

# проверим удаление всех элементов
print('Удаление всех элементов:')
head, tail = FNC.remove_from_front(head, tail)
head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_front(head, tail)
head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_front(head, tail)  # на этом моменте осталось 2 элемента, должен вернуть None, None
head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_front(head, tail)  # сейчас список пустой, должен вернуть None, None
head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail, end='\n\n')

# проверим удаление только с начала
print('Удаление всех элементов с начала:')
head = tail = None
head, tail = FNC.add_to_back(10, head, tail)
head, tail = FNC.add_to_back(20, head, tail)
head, tail = FNC.add_to_back(30, head, tail)
head, tail = FNC.add_to_front(5, head, tail)
head, tail = FNC.add_to_back(40, head, tail)
print('Изначальный список')
print('Голова и хвост:')
print(head, tail, end='\n\n')

head, tail = FNC.remove_from_front(head, tail)
print('Голова и хвост:')
print(head, tail)
head, tail = FNC.remove_from_front(head, tail)
print('Голова и хвост:')
print(head, tail)
head, tail = FNC.remove_from_front(head, tail)
print('Голова и хвост:')
print(head, tail)
head, tail = FNC.remove_from_front(head, tail)
print('Голова и хвост:')
print(head, tail)
head, tail = FNC.remove_from_front(head, tail)  # остался 1 элемент
print('Голова и хвост:')
print(head, tail)
head, tail = FNC.remove_from_front(head, tail)  # проверим как работает удалению для пустого списка
print('Голова и хвост:')
print(head, tail, end='\n\n')

# проверим удаление только с конца
print('Удаление всех элементов с конца:')
head = tail = None
head, tail = FNC.add_to_back(10, head, tail)
head, tail = FNC.add_to_back(20, head, tail)
head, tail = FNC.add_to_back(30, head, tail)
head, tail = FNC.add_to_front(5, head, tail)
head, tail = FNC.add_to_back(40, head, tail)
print('Изначальный список')
print('Голова и хвост:')
print(head, tail, end='\n\n')

head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_end(head, tail)
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_end(head, tail)  # остался 1 элемент
print('Голова и хвост:')
print(head, tail)

head, tail = FNC.remove_from_end(head, tail)  # проверим как работает удалению для пустого списка
print('Голова и хвост:')
print(head, tail, end='\n\n')

# Проверим функции на пустом списке
print('Элементы друг за другом:')
print(FNC.print_one_by_one(head, tail), end='\n\n')

print('Поиск элемента со значением 20:')
print(FNC.search(20, head, tail), end='\n\n')

print('Поиск элемента со значением 100:')
print(FNC.search(100, head, tail), end='\n\n')

print('Поиск элемента с индексом 0:')
print(FNC.get_by_index_1(0, head, tail), end='\n\n')

print('Поиск элемента с индексом 6:')
print(FNC.get_by_index_1(6, head, tail), end='\n\n')
