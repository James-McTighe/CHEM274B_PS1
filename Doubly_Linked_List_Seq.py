class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def is_empty(self):
        return self.head == None and self.tail == None

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)

        if self.head is None:
            self.head = node

        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node

    def delete_first(self):

        y = self.head
        x = y.next
        x.prev = None
        self.head = x
        del y
        return x

    def delete_last(self):
        y = self.tail
        x = y.prev
        x.next = None
        self.tail = x
        del y
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        node1 = Doubly_Linked_List_Node(x1)
        node2 = Doubly_Linked_List_Node(x2)

        L2.head = node1
        L2.tail = node2

        y1 = Doubly_Linked_List_Node(node1.prev)
        y2 = Doubly_Linked_List_Node(node2.next)
        y1.next = y2
        y2.prev = y1
        return L2

    def splice(self, x, L2):
        
        y = x.next
        x.next = L2.tail
        y.prev = L2.head

        # L2.head = None
        # L2.tail = None
       
