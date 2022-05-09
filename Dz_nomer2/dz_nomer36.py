from random import randint

"""В код двухсвязанного списка добавить следующее:



атрибут count_elements который бы хранил текущее кол-во элементов списка. После можно изменить функцию __len__
def __len__(self):
    return self.count_elements
    
добавить новые функции insert для вставки новых значений по индексу:
def insert_after_index(self, idx, value):
    pass

def insert_before_index(self, idx, value):
    pass
добавить новую функцию remove для удаления элемента по индексу:
def remove_by_index(self, idx):
    pass
Заготовки новых функций уже есть в коде. Осталось их только реализовать."""


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def __repr__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev_node):
        self.__prev = prev_node


class DoubleLinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.__count_elements = 0

        if values is not None:
            node = Node(value=values[0])
            self.head = node
            self.__count_elements += 1
            for i in range(1, len(values)):
                node.next = Node(value=values[i])
                node.next.prev = node
                node = node.next
                self.__count_elements += 1


            self.tail = node

    @property
    def count_elements(self):
        return self.__count_elements

    def __str__(self):
        node = self.head
        values = ['None']
        while node is not None:
            values.append(str(node.value))
            node = node.next
        values.append('None')

        return ' <-> '.join(values)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # def __count_elements(self):
    #     node = self.head
    #     while node is not None:
    #         node = node.next
    #         self.count_elements += 1
    #     return self.count_elements




    def __get_key_by_index(self, idx):
        current_idx = 0
        node = self.head
        while node is not None:
            if current_idx == idx:
                return node
            node = node.next
            current_idx += 1
        return None

    def __getitem__(self, idx):
        node = self.__get_key_by_index(idx)
        if node is None:
            raise IndexError('Index out of range')
        return node.value

    def __setitem__(self, idx, value):
        node = self.__get_key_by_index(idx)
        if node is None:
            raise IndexError('Index out of range')
        node.value = value

    def __len__(self):
        # current_idx = 0
        # node = self.head
        # while node is not None:
        #     node = node.next
        #     current_idx += 1
        # return current_idx
        return self.__count_elements

    def add_to_head(self, value):
        self.__count_elements += 1
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_to_tail(self, value):
        self.__count_elements += 1
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            return

        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def is_empty(self):
        if self.head is None:
            raise Exception('List is empty')

    def get_node_by_value(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                break
            node = node.next
        return node

    def insert_after(self, target_value, new_value):
        self.is_empty()
        node = self.get_node_by_value(target_value)

        if node is None:
            raise Exception(f'Node with value {target_value} not found')

        if node == self.tail:
            self.add_to_tail(new_value)
            return

        new_node = Node(new_value)
        new_node.prev = node
        new_node.next = node.next
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node
        self.__count_elements += 1

    def insert_before(self, target_value, new_value):
        self.is_empty()
        node = self.get_node_by_value(target_value)

        if node is None:
            raise Exception(f'Node with value {target_value} not found')

        if node == self.head:
            self.add_to_head(new_value)
            return

        new_node = Node(new_value)
        new_node.next = node
        new_node.prev = node.prev
        if node.prev is not None:
            node.prev.next = new_node
        node.prev = new_node
        self.__count_elements += 1

    def insert_after_index(self, idx, value):
        self.is_empty()
        node = self.get_node_by_value(value)

        if node is None:
            raise Exception(f'Node with value {value} not found')

        if node == self.tail:
            self.add_to_tail(value)
            return

        new_node = Node(value)
        new_node.prev = node
        new_node.next = node.next
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node
        self.__count_elements += 1
        pass

    def insert_before_index(self, idx, value):
        pass

    def remove(self, value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.next is None:
            if self.head.value == value:
                del self.head
                self.head = None
                self.__count_elements -= 1
                return
            else:
                raise Exception(f'Node with value {value} not found')

        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            self.__count_elements -= 1
            return

        node = self.get_node_by_value(value)
        if node is None:
            raise Exception(f'Node with value {value} not found')

        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.__count_elements -= 1
            del node
        else:
            if node.value == value:
                node.prev.next = None
                self.__count_elements -= 1
            else:
                raise Exception(f'Node with value {value} not found')


    def remove_by_index(self, idx):
        pass

    def revers(self):
        if self.head is None:
            raise Exception('List is empty')

        p = self.head
        q = p.next
        p.next = None
        p.prev = q

        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev

        self.head = p


dll1 = DoubleLinkedList()
print(dll1)
dll2 = DoubleLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(dll2)
print(dll2.get_node_by_value(1))
dll2.add_to_head(2)
print(dll2)
print(len(dll2))
dll2.insert_before(5,5)
print(dll2)
print(len(dll2))
dll2.insert_after(9,10)
print(dll2)
print(len(dll2))
dll2.remove(10)
print(dll2)
print(len(dll2))

