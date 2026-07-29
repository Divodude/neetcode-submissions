class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

       
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        
        cur = head
        for i in range(len(stack) // 2):
           
            back = stack.pop()
           
            nxt = cur.next
            cur.next = back
            back.next = nxt
            cur = nxt

        cur.next = None