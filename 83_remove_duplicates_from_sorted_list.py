from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        head_1 = self
        head_2 = other

        while head_1 is not None or head_2 is not None:
            print(head_1.val)
            print(head_2.val)

            assert head_1.val == head_2.val, f"Val_1 {head_1.val} Val_2 {head_2.val}"
            head_1 = head_1.next
            head_2 = head_2.next

    @classmethod
    def from_list(cls, l: list[int]) -> Optional["ListNode"]:
        if not l:
            return None
        if len(l) == 1:
            return cls(val=l[0])
        head = cls(val=l[0])
        temp = head
        for index in range(1, len(l)):
            next_ = cls(val=l[index])
            temp.next = next_
            temp = next_
        return head

    def __str__(self):
        head = self
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return str(res)


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head




in_ = [1,1,2,3,3]
out = [1,2,3]

print(Solution().delete_duplicates(ListNode.from_list(in_)))
print(ListNode.from_list(out))

# assert ListNode.from_list(in_) == ListNode.from_list(out)