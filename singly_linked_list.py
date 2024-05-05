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

    def prepend(self, data):
        new_node = node(data)
        cur = self.head
        self.head = new_node
        new_node.next = cur

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
                print("data : {0} index : {1}".format(data, cur_index))
                return
            cur_node = cur_node.next
            cur_index += 1

        print("there is no data about {}".format(data))
        return

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return

        if index == 0:
            self.head = self.head.next
            return

        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index - 1:
                cur_node.next = cur_node.next.next
                return
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
                    return
                else:
                    print("Cannot erase previous node.")
                    return
            prev_node = cur_node
            cur_node = cur_node.next

        print("No node with data '{}' found.".format(cur_data))
        return

    def erase_next(self, cur_data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                if cur_node.next:
                    cur_node.next = cur_node.next.next
                    return
                else:
                    print("Cannot erase next node.")
                    return
            cur_node = cur_node.next

        print("No node with data '{}' found.".format(cur_data))
        return

    def insert(self, index, insert_data):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        if index == 0:
            self.prepend(insert_data)
            return
        new_node = node(insert_data)
        cur_node = self.head
        cur_index = 0
        prev_node = None
        while cur_node:
            if cur_index == index:
                prev_node.next = new_node
                new_node.next = cur_node
                return
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
                return
            prev_node = cur_node
            cur_node = cur_node.next

        print("No node with data {} found.".format(cur_data))
        return

    def insert_next(self, cur_data, insert_data):
        new_node = node(insert_data)
        cur_node = self.head
        while cur_node:
            if cur_node.data == cur_data:
                new_node.next = cur_node.next
                cur_node.next = new_node
                return
            cur_node = cur_node.next
        print("No node with data {} found.".format(cur_data))
        return

    def main(self):
        self.display()
        self.append(1)
        self.append(4)
        self.append("a")
        self.display()
        "erase 1 index "
        self.prepend(5)
        self.get_data("a")
        self.insert_prev(1, 3)
        self.insert_next(1, 8)
        self.insert(1, 10)
        self.display()
        self.erase_next(10)
        self.erase_prev(10)
        self.display()


test_list = singly_linked_list()
test_list.main()