# Circular doubly linked list with head and tail
# Глобальные константы, обозначающие индексы в узле связанного списка
VALUE = 0
NEXT = 1
PREV = 2


# Добавление в конец
def add_to_back(value, head, tail):
    item = [value, None, None]
    if head is None:
        head = tail = item
    else:
        tail[NEXT] = item
        item[PREV] = tail
        tail = item
    head[PREV] = item
    item[NEXT] = head
    return head, tail


# Добавление в начало
def add_to_front(value, head, tail):
    item = [value, None, None]
    if head is None:
        head = tail = item
    else:
        head[PREV] = item
        item[NEXT] = head
        head = item
    tail[NEXT] = item
    item[PREV] = head
    return head, tail


# Удалить элемент с начала, возвращает tail и новый head
def remove_from_front(head, tail):
    if head is None and tail is None:
        return head, tail
    elif head == tail:
        head = None
        tail = None
        return head, tail
    else:
        h1 = head[NEXT]
        h1[PREV] = tail
        tail[NEXT] = h1
        head = h1
        return head, tail


# Удалить элемент с конца, возвращает head и новый tail
def remove_from_end(head, tail):
    if head is None and tail is None:
        return head, tail
    elif head == tail:
        head = None
        tail = None
        return head, tail
    else:
        t1 = tail[PREV]
        t1[NEXT] = head
        head[PREV] = t1
        tail = t1
        return head, tail


# Печать элементов друг за другом
def print_one_by_one(head, tail):
    if head == tail is None:
        return 'Невозможно.Пустой список'
    else:
        h1 = head
        while h1[NEXT] != head:
            print(h1)
            h1 = h1[NEXT]
        return tail


# Поиск элемента по значению, возвращает связку из элемента, предыдущего и следующего элемента
def search(value, head, tail):
    if head == tail is None:
        return 'Невозможно.Пустой список'
    else:
        res = None
        item = [value, None, None]
        h1 = head
        if item[VALUE] == head[VALUE]:
            res = head
        elif item[VALUE] == tail[VALUE]:
            res = tail
        else:
            while h1[NEXT] != head:
                if item[VALUE] == h1[VALUE]:
                    res = h1
                h1 = h1[NEXT]
        if res is None:
            return 'Такого элемента нет'
        else:
            return res


# Поиск элемента по индексу, возвращает связку из элемента, предыдущего и следующего элемента
def get_by_index_1(index, head, tail):
    i = 0
    h1 = head
    h2 = head
    len_lst = 0
    if head is not None and tail is not None:
        while h2[NEXT] != head:
            h2 = h2[NEXT]
            len_lst += 1
    if head == tail is None:
        return 'Невозможно.Пустой список'
    elif len_lst < index or index < 0:
        return 'Ошибка'
    else:
        if index == 0:
            return h1
        else:
            while True:
                h1 = h1[NEXT]
                i += 1
                if i == index:
                    break
            return h1
