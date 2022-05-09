class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

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

    def __repr__(self):
        return str(self.__value)


class SingleLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            copy_lst = nodes.copy()
            node = Node(value=copy_lst.pop(0))
            self.head = node
            for elem in copy_lst:
                node.next = Node(value=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")

        return '-->'.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_head(self, value):
        node = Node(value=value)
        node.next = self.head
        self.head = node

    def add_to_tail(self, value):
        node = Node(value=value)
        if self.head is None:
            self.head = node
            return

        current_node = None
        for current_node in self:
            pass
        current_node.next = node

    def insert_after(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        new_node = Node(value=new_value)
        for node in self:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with {target_value} not found')

    def insert_before(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.value == target_value:
            self.add_to_head(new_value)
            return

        new_node = Node(value=new_value)
        prev_node = self.head
        for node in self:
            if node.value == target_value:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with {target_value} not found')

    def insert_by_number_after(self, element_number, new_value):
        if self.head is None:
            raise Exception('List is empty')

        counter = 1
        new_node = Node(value=new_value)
        for node in self:
            if counter == element_number:
                new_node.next = node.next
                node.next = new_node
                return
            counter += 1

        raise Exception(f'Node with number {element_number} not found')

    def insert_by_number_before(self, element_number, new_value):
        if self.head is None:
            raise Exception('List is empty')

        if element_number == 1:
            self.add_to_head(new_value)
            return

        counter = 1
        new_node = Node(value=new_value)
        prev_node = self.head
        for node in self:
            if counter == element_number:
                prev_node.next = new_node
                new_node.next = node
                return
            counter += 1
            prev_node = node

        raise Exception(f'Node with number {element_number} not found')

    def remove_by_number(self, element_number):
        if self.head is None:
            raise Exception('List is empty')

        if element_number == 1:
            new_head = self.head.next
            del self.head
            self.head = new_head
            return

        counter = 1
        prev_node = self.head
        for node in self:
            if counter == element_number:
                prev_node.next = node.next
                del node
                return
            counter += 1
            prev_node = node

        raise Exception(f'Node with number {element_number} not found')


single_list_2 = SingleLinkedList([1, 2, 3, 4, 5])
print(single_list_2)


single_list_2.insert_by_number_after(5,23)
print(single_list_2)
single_list_2.insert_by_number_before(1,25)
print(single_list_2)
single_list_2.remove_by_number(3)
print(single_list_2)

