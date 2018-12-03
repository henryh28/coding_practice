// Complete the compareTriplets function below.
static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
    List<Integer> answer = new ArrayList<>();
    answer.add(0);
    answer.add(0);

    for (int i = 0; i < a.size(); i++) {
        if (a.get(i) > b.get(i)) {
            answer.set(0, answer.get(0) + 1);
        } else if (b.get(i) > a.get(i)) {
            answer.set(1, answer.get(1) + 1);
        }
    }

    return (answer);
}
