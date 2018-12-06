// ================== java solution ==================================
static int stringConstruction(String s) {
    Map<Character, Integer> letters = new HashMap();

    for (int i = 0; i < s.length(); i ++) {
        char key = s.charAt(i);
        letters.put(key, letters.containsKey(key) ? letters.get(key) + 1 : 1);
    }

    return (letters.size());
}

// ================== python solution ==================================
def stringConstruction(s):
    letters = {}

    for letter in s:
        letters[letter] = 1 if letter not in letters else letters[letter] + 1

    return len(letters)
