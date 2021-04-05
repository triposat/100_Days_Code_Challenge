class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Reverse_Linked_List:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

    def Reverse_list(self):
        previous = None
        current = self.head
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous

    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    Lin_list = Reverse_Linked_List()
    num = int(input("How many elements: "))
    for i in range(num):
        ele = int(input())
        Lin_list.push(ele)
    print("Linked List:")
    Lin_list.Display()
    Lin_list.Reverse_list()
    print("\nReverse Linked List: ")
    Lin_list.Display()
