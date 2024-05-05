class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return None

    def prepend(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        return None

    def length(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(str(cur_node.data))
            cur_node = cur_node.next
        print(" <-> ".join(elements))
        return None

    def display_reverse(self):
        elements = []
        cur_node = self.tail
        while cur_node:
            elements.append(str(cur_node.data))
            cur_node = cur_node.prev
        print(" <-> ".join(elements))
        return None

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_index += 1

    def get_data(self, data):
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                print(f"data : {data} index : {cur_index}")
                return
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_index += 1

    def get_data(self, data):
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                print(f"data : {data} index : {cur_index}")
                return cur_node.data, cur_index
            cur_node = cur_node.next
            cur_index += 1

        raise ValueError(f"Data {data} not found in the list.")

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
        cur_node = self.head
        cur_index = 0
        while cur_node:
            if cur_index == index:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev= cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                    if self.head:
                        self.head.prev = None
                if cur_node == self.tail:
                    self.tail = cur_node.prev
                    if self.tail:
                        self.tail.next = None
                return None
            cur_node = cur_node.next
            cur_index += 1

    def erase_prev(self, cur_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                if cur_node.prev is None:
                    print(f"No previous node exists for the first node with data {cur_data}.")
                    return None

                deleted_node = cur_node.prev
                if deleted_node:
                    if deleted_node.prev:
                        deleted_node.prev.next = cur_node
                    else:
                        self.head = cur_node
                    cur_node.prev = deleted_node.prev
                    return None
            cur_node = cur_node.next
        print(f"No node with data {cur_data} found.")
        return None

    def erase_next(self, cur_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                if cur_node.next is None:
                    print(f"No next node exists for the last node with data {cur_data}.")
                    return None
                else:
                    deleted_node = cur_node.next
                    if deleted_node.next:
                        deleted_node.next.prev = cur_node
                    cur_node.next = deleted_node.next
                    if deleted_node == self.tail:
                        self.tail = cur_node
                    return None
            cur_node = cur_node.next
        print(f"No node with data {cur_data} found.")
        return None

    def insert_next(self, cur_data, new_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                new_node = node(new_data)
                if cur_node.next:
                    new_node.next = cur_node.next
                    cur_node.next.prev = new_node
                else:
                    self.tail = new_node
                new_node.prev = cur_node
                cur_node.next = new_node
                return None
            cur_node = cur_node.next
        print(f"No node with data {cur_data} found.")
        return None

    def insert_prev(self, cur_data, new_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                new_node = node(new_data)
                if cur_node.prev:
                    new_node.prev = cur_node.prev
                    cur_node.prev.next = new_node
                else:
                    self.head = new_node
                new_node.next = cur_node
                cur_node.prev = new_node
                return None
            cur_node = cur_node.next
        print(f"No node with data {cur_data} found.")
        return None

    def main(self):
        self.append(1)
        self.append(4)
        self.append("a")
        self.display()
        self.display_reverse()
        self.prepend("b")
        self.display()
        self.erase_prev("b")
        self.erase_next("a")
        self.display()
        self.erase_prev(1)
        self.erase_next(1)
        self.display()
        self.insert_prev(1, "b")
        self.insert_next(1, 4)
        self.display()
        try:
            data, index = self.get_data('b')
            print(f"Data: {data}, Index: {index}")
        except ValueError as err:
            print(err)


test_list = doubly_linked_list()
test_list.main()