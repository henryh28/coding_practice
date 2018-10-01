def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    ans_p, ans_q = [], []
    
    if p == q:
      return (True)
    
    def traverse(node, answer):
      answer.append(node.val if node else "null")
      answer.append(traverse(node.left, answer) if node.left else "null")
      answer.append(traverse(node.right, answer) if node.right else "null")
      
    if p and q:
      traverse(p, ans_p)
      traverse(q, ans_q)
    else:
      return (False)
    
    return (ans_p == ans_q)
    