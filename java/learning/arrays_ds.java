// Complete the reverseArray function below.
static int[] reverseArray(int[] a) {
    int answer[] = new int[a.length];

    for (int i = a.length - 1, j = 0; i >= 0; i--, j++) {
        answer[j] = a[i];
    }

    return (answer);
}
