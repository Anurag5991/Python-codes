#Definition for singly-linked list.
import types
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

# def addTwoNumbers(l1, l2):

    # normal list solution: 
        # l1.reverse()
        # if l1[0] == 0:
        #     print("not possible")
        # list1 = l1.copy()
        # l2.reverse()
        # if l2[0] == 0:
        #     print("not possible")
        # list2 = l2.copy()
        # num1 = ''
        # num2 = ''
        # for i in list1:
        #     num1 += str(i)
        # num3 = int(num1)
        # for j in list2:
        #     num2 += str(j)
        # num4 = int(num2)
        # num5 = str(num3 + num4)
        # list3 = []
        # for i in num5:
        #     list3.append(i)
        # list3.reverse()
        # return list3

    # linked list method
        added = ListNode(val = (l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10
        current_node = added

        
        while( l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next

            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next

        while( l1.next):
            l1 = l1.next
            

            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next


        while(l2.next):
            
            l2 = l2.next

            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next

        if(carry_over) > 0:
            current_node.next = ListNode(val=1)

        return added

xyz = Solution()
print(xyz.addTwoNumbers([1,0,2], [2,0,2]))