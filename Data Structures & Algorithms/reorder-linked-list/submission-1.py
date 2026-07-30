from typing import Optional

# Assuming ListNode definition exists in the environment:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Reorders a singly linked list from [0, 1, 2, ..., n-1] 
    to [0, n-1, 1, n-2, 2, n-3, ...]
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the list in place. The return type is None because it modifies the list structure.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list (Slow/Fast Pointer approach)
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' is now at the start of the second half.
        # We need to break the link between the first and second halves.
        second_half_head = slow.next
        slow.next = None  # Terminate the first half

        # Step 2: Reverse the second half
        prev = None
        current = second_half_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # 'prev' is now the head of the reversed second half (e.g., n-1, n-2, ...)
        reversed_second_half = prev

        # Step 3: Merge/Interleave the two halves
        head1 = head
        head2 = reversed_second_half
        
        while head2 and head1 and head1.next:
            # Save next pointers before rewiring
            temp1 = head1.next
            temp2 = head2.next
            
            # Interleave: 
            # 1. Link current node of first half to the current node of second half
            head1.next = head2
            
            # 2. Link current node of second half back to the next node of the first half
            head2.next = temp1
            
            # Move pointers forward for the next iteration
            head1 = temp1  # Next node in original first half
            head2 = temp2  # Next node in reversed second half

        # The reordering is done in place, so we don't need to return anything.
        return 

