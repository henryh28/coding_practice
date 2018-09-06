def isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    integer, floaty = None, None
    
    try:
      integer = int(s)
    except:
      pass
      
    try:
      floaty = float(s)
    except:
      pass

    return True if integer != None or floaty != None else False
    