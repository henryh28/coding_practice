// ================== java solution ====================
static int palindromeIndex(String s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) {
            StringBuilder remove_left = new StringBuilder();
            remove_left.append(s.substring(0, left)).append(s.substring(left + 1, s.length()));
            if (remove_left.toString().equals(remove_left.reverse().toString())) {
                return (left);
            }

            StringBuilder remove_right = new StringBuilder();
            remove_right.append(s.substring(0, right)).append(s.substring(right + 1, s.length()));
            if (remove_right.toString().equals(remove_right.reverse().toString())) {
                return (right);
            }
            return (-1);
        }
        left += 1;
        right -= 1;
    }
    return (-1);
}

// ================== python solution ====================
def palindromeIndex(s):
  left = 0
  right = len(s) - 1
  
  while left < right:
    if s[left] != s[right]:
      remove_left = s[:left] + s[left + 1:]
      if remove_left == remove_left[::-1]:
        return left

      remove_right = s[:right] + s[right + 1:]
      if remove_right == remove_right[::-1]:
        return right
      
      return -1
    
    left += 1
    right -= 1

  return -1
