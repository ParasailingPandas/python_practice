class list_node: 
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def value(self):
        return self.data

class linked_list:
    def __init__(self):
        self.head = None 

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value())
            current = current.next

    def prepend(self, data):
        self.head = list_node(data, self.head)


mylist = linked_list()
mylist.prepend(5)
mylist.prepend(4)
mylist.prepend(10)
mylist.prepend(33)
mylist.print_list()