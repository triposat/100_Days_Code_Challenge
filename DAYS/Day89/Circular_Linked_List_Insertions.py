class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_Linked_List:
    def __init__(self):
        self.last = None

    def Add_to_Empty(self, data):
        if self.last is not None:
            return self.last
        temp = Node(data)
        self.last = temp
        self.last.next = self.last
        return self.last

    def Add_to_Begin(self, data):
        if self.last is None:
            return self.Add_to_Empty(data)
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        return self.last

    def Add_to_End(self, data):
        if self.last is None:
            return self.Add_to_Empty(data)
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
        return self.last

    def Add_After(self, data, key):
        if self.last == None:
            return None
        temp = Node(data)
        temp1 = self.last.next
        while temp1:
            if temp1.data == key:
                temp.next = temp1.next
                temp1.next = temp
                if temp1 == self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            temp1 = temp1.next
            if temp1 == self.last.next:
                print(data, "Not present in a list!")
                break

    def Display(self):
        if self.last == None:
            print("List is Empty!")
            return
        temp = self.last.next
        temp1 = temp
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
            if temp == self.last.next:
                print(temp1.data)
                break


if __name__ == "__main__":

    L_list = Circular_Linked_List()
    L_list.Add_to_Empty(6)
    L_list.Add_to_Begin(4)
    L_list.Add_to_Begin(2)
    L_list.Add_to_End(8)
    L_list.Add_to_End(12)
    L_list.Add_After(10, 8)
    L_list.Display()
