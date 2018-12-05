// ============= java solution ==============
static int equalizeArray(int[] arr) {
    int high = 0;
    int total = 0;
    Map<Integer, Integer> value_dict = new HashMap();

    for (int i = 0; i < arr.length; i++) {
        int key = arr[i];
        value_dict.put(key, value_dict.containsKey(key) ? (int)value_dict.get(key) + 1 : 1);
    }

    for (Map.Entry<Integer, Integer> entry : value_dict.entrySet()) {
        high = Math.max(high, entry.getValue());
        total += entry.getValue();
    }

    return (total - high);
}



// ============= python solution ==============
def equalizeArray(arr):
  value_dict = {}
  high, total = 0, 0

  for num in arr:
    value_dict[num] = 1 if num not in value_dict else value_dict[num] + 1

  for k, v in value_dict.items():
    high = max(high, v)
    total += v

  return (total - high)
  
