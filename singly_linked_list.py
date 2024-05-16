class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        return None

    def prepend(self, data):
        new_node = node(data)
        cur = self.head
        self.head = new_node
        new_node.next = cur
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
        print(" -> ".join(elements))
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
                return cur_node.data, cur_index
            cur_node = cur_node.next
            cur_index += 1

        raise ValueError(f"Data {data} not found in the list.")

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None

        if index == 0:
            erased_node = self.head
            self.head = self.head.next
            return erased_node, index

        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index - 1:
                erased_node = cur_node.next
                cur_node.next = cur_node.next.next
                return erased_node, index
            cur_node = cur_node.next
            cur_index += 1

    def erase_prev(self, cur_data):
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data == cur_data:
                if prev_node:
                    if prev_node == self.head:
                        self.head = cur_node
                    else:
                        prev_node.next = cur_node.next
                    return None
                else:
                    print("Cannot erase previous node.")
                    return None
            prev_node = cur_node
            cur_node = cur_node.next

        print(f"No node with data {cur_data} found.")
        return None

    def erase_next(self, cur_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                if cur_node.next:
                    cur_node.next = cur_node.next.next
                    return None
                else:
                    print("Cannot erase next node.")
                    return None
            cur_node = cur_node.next

        print(f"No node with data {cur_data} found.")
        return None

    def insert(self, index, insert_data):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        if index == 0:
            self.prepend(insert_data)
            return None
        new_node = node(insert_data)
        cur_node = self.head
        cur_index = 0
        prev_node = None
        while cur_node:
            if cur_index == index:
                prev_node.next = new_node
                new_node.next = cur_node
                return None
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index += 1

    def insert_prev(self, cur_data, insert_data):
        new_node = node(insert_data)
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data == cur_data:
                new_node.next = cur_node
                if prev_node:
                    prev_node.next = new_node
                else:
                    self.head = new_node
                return None
            prev_node = cur_node
            cur_node = cur_node.next

        print(f"No node with data {cur_data} found.")
        return None

    def insert_next(self, cur_data, insert_data):
        new_node = node(insert_data)
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                new_node.next = cur_node.next
                cur_node.next = new_node
                return None
            cur_node = cur_node.next
        print(f"No node with data {cur_data} found.")
        return None

def main():
    test_list = singly_linked_list()
    test_list.display()
    test_list.append(1)
    test_list.append(4)
    test_list.append("a")
    test_list.display()
    "erase 1 index "
    test_list.prepend(5)
    test_list.get_data("a")
    test_list.insert_prev(1, 3)
    test_list.insert_next(1, 8)
    test_list.insert(1, 10)
    test_list.display()
    test_list.erase_next(10)
    test_list.erase_prev(10)
    test_list.display()
    erased_node, index = test_list.erase(2)
    print(f"Index : {index} Data : {erased_node.data} has been removed")
    test_list.display()
    try:
        data, index = test_list.get_data('a')
        print(f"Data: {data}, Index: {index}")
    except ValueError as err:
        print(err)


main()