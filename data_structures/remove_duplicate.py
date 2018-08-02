# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        
        # Helper function to return the next unique value starting from argument, self inclusive
        def next_unique(node):
            current = memory = node
            
            while current != None:
                # Next value is different from current value, current is unique
                if current.next and current.next.val != current.val:
                    return (current)
                # Hit end of linked list, but current value is unique
                elif current.next == None: 
                    return (current)
                # Next value same as current value, advance til current is a different value
                else:
                    memory = current.val
                    while current.val == memory:
                        if current.next != None:
                            current = current.next
                        else:
                            return (None)
    
        # Ensure first node is unique
        head = current = next_unique(current)
    
        # head is unique now, loop process the remainder nodes
        while current != None:
            current.next = next_unique(current.next)
            current = current.next
            
            if current == None or current.next == None:
                break
        
        
        return (head)
