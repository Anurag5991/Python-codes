class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        count = self.head
        listr = ""
        while count:
            listr += str(count.val) + '-->'
            count = count.next
        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        count = self.head
        while count.next:
            count = count.next

        count.next = Node(data, None)

    def insert_values(self,values):
        self.head = None
        for i in values:
            self.insert_at_end(i)

    def get_length(self):
        len = 0
        if self.head is None:
            print("length of linked list is zero")
        count = self.head
        while count:
            len += 1
            count = count.next
        return len

    def remove_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_values([2,3,4])
    print(ll.get_length())
    print(ll.insert_at_index(3, 23))

    ll.print()
        



    

