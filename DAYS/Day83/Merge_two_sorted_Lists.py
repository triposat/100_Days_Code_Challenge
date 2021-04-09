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

    def Merge(self, List_1, List_2):
        temp = head = Node(0)
        while True:
            if List_1 is None:
                temp.next = List_2
                break
            if List_2 is None:
                temp.next = List_1
                break
            if List_1.data <= List_2.data:
                temp.next = List_1
                List_1 = List_1.next
            else:
                temp.next = List_2
                List_2 = List_2.next
            temp = temp.next
        return head.next

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list_1 = Linked_List()
    L_list_2 = Linked_List()

    L_list_1.Insert_At_End(5)
    L_list_1.Insert_At_End(8)
    L_list_1.Insert_At_End(10)

    L_list_2.Insert_At_End(7)
    L_list_2.Insert_At_End(9)
    L_list_2.Insert_At_End(11)
    L_list_2.Insert_At_End(12)

    L_list_3 = Linked_List()
    L_list_3.head = L_list_3.Merge(L_list_1.head, L_list_2.head)

    L_list_3.Display()
