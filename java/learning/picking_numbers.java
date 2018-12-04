// ================= java solution ===============
public static int pickingNumbers(List<Integer> a) {
    int answer = 0;
    Map<Integer, Integer> value_dict = new HashMap();

    for (int i = 0; i < a.size(); i++) {
        int key = a.get(i);
        value_dict.put(key, value_dict.containsKey(key) ? (int)value_dict.get(key) + 1 : 1);
    }

    for (Map.Entry<Integer, Integer> kv : value_dict.entrySet()) {
        answer = Math.max(answer, kv.getValue());
        if (value_dict.get(kv.getKey() + 1) != null) {
            answer = Math.max(answer, kv.getValue() + value_dict.get(kv.getKey() + 1));
        }

        if (value_dict.get(kv.getKey() - 1) != null) {
            answer = Math.max(answer, kv.getValue() + value_dict.get(kv.getKey() - 1));
        }
    }

    return (answer);
}

// ================= python solution ===============
def pickingNumbers(a):
  value_dict = {}
  answer = 0

  for num in a:
    value_dict[num] = 1 if num not in value_dict else value_dict[num] + 1

  for k, v in value_dict.items():
    answer = max(answer, max(v + value_dict.get(k - 1, 0), v + value_dict.get(k + 1, 0)))

  return (answer)
