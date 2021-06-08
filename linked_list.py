class node:
    """
    This is a abstract class
    """
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def append_right(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def append_left(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def show_linked_list(self):
        current_node = self.head
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)



Linked_list = linked_list()
Linked_list.append_right(5)
Linked_list.append_right(53)
Linked_list.append_right(65)
Linked_list.append_right(56)
Linked_list.append_right(56)
Linked_list.append_right(696)
Linked_list.append_left(99999)
Linked_list.show_linked_list()
