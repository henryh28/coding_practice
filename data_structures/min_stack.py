class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        lowest = None if len(self.stack) == 0 else min(x, self.stack[-1][1])
        
        if lowest == None:
          lowest = x
        
        self.stack.append((x, lowest))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        