# python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Pointer:
    def __init__(self, lvalue = None):
        # lvalue is "locator value" similar in C programming language
        self.to = lvalue
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        plist1 = Pointer(list1); plist2 = Pointer(list2); 
        pChosenNode = None; 
        head = currNode = ListNode()
        while plist1.to and plist2.to:
            pChosenNode = plist1 if plist1.to.val < plist2.to.val else plist2
            currNode.next = pChosenNode.to
            currNode = currNode.next
            pChosenNode.to = pChosenNode.to.next # list1 = list1.next, list2 = list1.to
        currNode.next = plist1.to or plist2.to
        return head.next
