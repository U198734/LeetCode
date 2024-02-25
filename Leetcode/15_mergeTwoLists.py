class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        current = dummy

        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val <= list2.val:
                # Append the smaller value to the merged list
                current.next = list1
                # Move the pointer in list1 forward
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the pointer in the merged list forward
            current = current.next

        # Append the remaining nodes from list1 or list2 (if any)
        current.next = list1 if list1 else list2

        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
