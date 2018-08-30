class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = []
        
        while l1 or l2:
          if l1 and l2:
            if l1.val > l2.val:
              answer.append(l2.val)
              l2 = l2.next
            else:
              answer.append(l1.val)
              l1 = l1.next
          else:
            if l1:
              answer.append(l1.val)
              l1 = l1.next
            else:
              answer.append(l2.val)
              l2 = l2.next
            
        return (answer)
        