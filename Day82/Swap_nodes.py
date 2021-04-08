class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def Insert_At_End(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def Swap(self, key1, key2):
        Prev_node_1 = None
        Prev_node_2 = None
        Node_1 = self.head
        Node_2 = self.head
        if self.head == None:
            return
        if key1 == key2:
            return
        while(Node_1.data != key1):
            Prev_node_1 = Node_1
            Node_1 = Node_1.next
        while(Node_2.data != key2):
            Prev_node_2 = Node_2
            Node_2 = Node_2.next
        if Prev_node_1 is not None:
            Prev_node_1.next = Node_2
        else:
            self.head = Node_2
        if Prev_node_2 is not None:
            Prev_node_2.next = Node_1
        else:
            self.head = Node_1
        temp = Node_1.next
        Node_1.next = Node_2.next
        Node_2.next = temp

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_End(8)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(10)
    L_list.Insert_At_End(7)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(11)
    L_list.Insert_At_End(9)
    print("Linked List: ")
    L_list.Display()
    print("Swap List: ")
    L_list.Swap(8, 5)
    L_list.Display()
