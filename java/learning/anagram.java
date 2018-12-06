// ================= java solution =====================
static int anagram(String s) {
    if (s.length() % 2 != 0) {
        return (-1);
    }

    Map<Character, Integer> pre_dict = new HashMap();
    Map<Character, Integer> post_dict = new HashMap();
    int matched = 0;

    for (int i = 0; i < s.length() / 2; i++) {
        char key = s.charAt(i);
        pre_dict.put(key, pre_dict.containsKey(key) ? pre_dict.get(key) + 1 : 1);
    }

    for (int i = (s.length() / 2); i < s.length(); i++) {
        char key = s.charAt(i);
        post_dict.put(key, post_dict.containsKey(key) ? post_dict.get(key) + 1 : 1);
    }

    for (Map.Entry<Character, Integer> kv : pre_dict.entrySet()) {
        if (post_dict.containsKey(kv.getKey())) {
            matched += Math.min(kv.getValue(), post_dict.get(kv.getKey()));
        }
    }

    return ((s.length() / 2) - matched);
}

// ================= python solution =====================
def anagram(s):
    if len(s) % 2 != 0:
        return -1

    pre_dict, post_dict = {}, {}
    matched = 0

    for letter in s[:len(s) // 2]:
        pre_dict[letter] = 1 if letter not in pre_dict else pre_dict[letter] + 1

    for letter in s[len(s) // 2:]:
        post_dict[letter] = 1 if letter not in post_dict else post_dict[letter] + 1

    for k, v in pre_dict.items():
        if k in post_dict:
            matched += min(v, post_dict[k])

    return len(s) // 2 - matched
