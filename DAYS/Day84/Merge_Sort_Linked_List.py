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

    def Sorted_Merging(self, left, right):
        Result = None
        if left == None:
            return right
        if right == None:
            return left
        if left.data <= right.data:
            Result = left
            Result.next = self.Sorted_Merging(left.next, right)
        else:
            Result = right
            Result.next = self.Sorted_Merging(right.next, left)
        return Result

    def Merge_Sort(self, link):
        if link == None or link.next == None:
            return link
        middle = self.get_Middle(link)
        next_to_middle = middle.next
        middle.next = None
        left = self.Merge_Sort(link)
        right = self.Merge_Sort(next_to_middle)
        Result = self.Sorted_Merging(left, right)
        return Result

    def get_Middle(self, link):
        if link == None:
            return link
        prev = link
        while(link.next != None and link.next.next != None):
            prev = prev.next
            link = link.next.next
        return prev

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list_1 = Linked_List()

    L_list_1.Insert_At_End(5)
    L_list_1.Insert_At_End(8)
    L_list_1.Insert_At_End(10)

    L_list_1.Insert_At_End(7)
    L_list_1.Insert_At_End(9)
    L_list_1.Insert_At_End(11)
    L_list_1.Insert_At_End(12)

    L_list_1.Merge_Sort(L_list_1.head)

    L_list_1.Display()
