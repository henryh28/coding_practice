// =============== java solution ================
static int beautifulTriplets(int d, int[] arr) {
    int answer = 0;
    Map<Integer, Integer> numbers = new HashMap();

    for (int i = 0; i < arr.length; i++) {
        int key = arr[i];
        numbers.put(key, numbers.containsKey(key) ? numbers.get(key) + 1 : 1);
    }

    for (Map.Entry<Integer, Integer> kv : numbers.entrySet()) {
        if (numbers.get(kv.getKey() + d) != null && numbers.get(kv.getKey() + d + d) != null) {
            answer += kv.getValue();
        }
    }

    return (answer);
}

// =============== python solution ================
def beautifulTriplets(d, arr):
    numbers = {}
    answer = 0

    for num in arr:
        numbers[num] = 1 if num not in numbers else numbers[num] + 1
    
    for k, v in numbers.items():
        if k + d in numbers and k + d + d in numbers:
            answer += v

    return (answer)
    
