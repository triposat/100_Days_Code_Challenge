import gc


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def Add_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def Delete_Node(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        gc.collect()

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    L_list = Doubly_Linked_List()
    L_list.Add_at_front(5)
    L_list.Add_at_front(7)
    L_list.Add_at_front(9)
    L_list.Add_at_front(8)
    L_list.Add_at_front(1)
    L_list.Add_at_front(2)
    print("Original Linked List: ")
    L_list.Display()
    L_list.Delete_Node(L_list.head)
    L_list.Delete_Node(L_list.head.next)
    L_list.Delete_Node(L_list.head.next)
    print("\nDelete Linked List: ")
    L_list.Display()