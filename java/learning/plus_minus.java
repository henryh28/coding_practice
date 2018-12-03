// Complete the plusMinus function below.
static void plusMinus(int[] arr) {
    float pos = 0;
    float neg = 0;
    float zero = 0;

    for (int i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            pos += 1;
        } else if (arr[i] < 0) {
            neg += 1;
        } else {
            zero += 1;
        }
    }

    System.out.format("%f%n%f%n%f%n", pos / arr.length, neg / arr.length, zero / arr.length);
}
