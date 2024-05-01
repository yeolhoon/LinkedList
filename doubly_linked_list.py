class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.before = None


class doubly_linked_list:
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
            new_node.before = cur

    def prepend(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            self.head.before = new_node
            new_node.next = self.head
            self.head = new_node

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
            elements.append(cur_node.data)
            cur_node = cur_node.next
        print(elements)

    def display_reverse(self):
        elements = []
        cur_node = self.head
        if cur_node:
            while cur_node.next:
                cur_node = cur_node.next
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.before
        print(elements)

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

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index:
                if cur_node.before:
                    cur_node.before.next = cur_node.next
                if cur_node.next:
                    cur_node.next.before = cur_node.before
                if cur_index == 0:  # Head is being erased
                    self.head = cur_node.next
                return
            cur_node = cur_node.next
            cur_index += 1


test_list = doubly_linked_list()
test_list.append(1)
test_list.append(4)
test_list.append("a")
test_list.display()
test_list.display_reverse()
test_list.prepend("b")
test_list.display()
test_list.display_reverse()
test_list.get(2)
test_list.erase(2)
test_list.display()