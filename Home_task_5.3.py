import random

# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# класс LinkedList для определиня связанного списка
class LinkedList:
    def __init__(self):  # определение элементов
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):  # создание строки для распечатки
        if self.first != None:
            current = self.first
            out_string = 'LinkedList: (' + str(current.value) #+ str(current.next)
            while current.next != None:
                current = current.next
                out_string += '), (' + str(current.value) #+ str(current.next)
            return out_string + ')'
        return 'LinkedList [is empty]'

    def clear(self):  # очистка списка
        self.__init__()

    def add(self, x):  # добавление элементов в конец списка
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    def len(self):
        length = 0
        if self.first:
            current = self.first
            while current.next:
                current = current.next
                length += 1
            length += 1  # +1 для учета self.first
        return length

first_list = LinkedList()
[first_list.add(random.randint(-15, 15)) for i in range(15)]
print("first_list: ", first_list)
print("first_list length: ", first_list.len())

second_list = LinkedList()
print("second_list: ", second_list)
print("second_list length: ",second_list.len())
