# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        car = 0

        cur = result

        while l1 or l2 or car > 0:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + car

            car = s // 10
            val = s % 10

            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next