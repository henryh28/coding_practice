class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        order = []
        
        for x in lists:
          current = x
          
          while current != None:
            order.append(current.val)
            current = current.next
        
        order.sort()
        return(order)
      