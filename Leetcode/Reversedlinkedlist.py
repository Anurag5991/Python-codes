class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def reverseList(self):
        prv = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        self.head = prv
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

first = LinkedList()
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print("First List is ")
first.printList()


first.reverseList()
print("\nResultant list is ")
first.printList()

