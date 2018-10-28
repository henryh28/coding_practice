class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next == None:
          return (False)
        
        fast = head.next
        slow = head

        while fast != slow:
          if fast.next == None or fast.next.next == None:
            return (False)
          
          fast = fast.next.next
          slow = slow.next

        return (True)
