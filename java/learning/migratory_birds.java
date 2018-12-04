// Complete the migratoryBirds function below.
static int migratoryBirds(List<Integer> arr) {
    Map birds = new HashMap();
    int most = 0;
    int answer = 0;

    for (int i = 0; i < arr.size(); i++) {
        int bird = arr.get(i);
        birds.put(bird, birds.containsKey(bird) ? (int)birds.get(bird) + 1 : 1);

        if ((int)birds.get(bird) == most) {
            answer = Math.min(most, bird);
        } else if ((int)birds.get(bird) > most) {
            most = (int)birds.get(bird);
            answer = bird;
        }
    }

    return (answer);
}

// ================ Comparison python solution =================
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds = {}
    most, answer = 0, 0

    for bird in arr:
        birds[bird] = 1 if bird not in birds else birds[bird] + 1

        if birds[bird] == most:
            answer = min(bird, answer)
        elif birds[bird] > most:
            most = birds[bird]
            answer = bird

    return (answer)
