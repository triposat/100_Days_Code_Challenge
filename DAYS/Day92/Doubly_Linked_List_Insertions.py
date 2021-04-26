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

    def Add_After(self, prev_node, new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def Add_End(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while(temp.next is not None):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def Display(self):
        temp = self.head
        print("\nTraversal in Forward Direction: ")
        while temp:
            print(temp.data, end=" ")
            last = temp
            temp = temp.next
        print("\nTraversal in Reverse Direction: ")
        while last:
            print(last.data, end=" ")
            last = last.prev
        print("\n")


if __name__ == "__main__":
    L_list = Doubly_Linked_List()
    L_list.Add_at_front(5)
    L_list.Add_at_front(7)
    L_list.Add_at_front(9)
    L_list.Add_at_front(8)
    L_list.Add_End(2)
    L_list.Add_End(6)
    L_list.Add_After(L_list.head.next, 1)
    L_list.Display()