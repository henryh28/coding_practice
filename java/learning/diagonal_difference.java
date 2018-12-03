// Complete the diagonalDifference function below.
static int diagonalDifference(int[][] arr) {
    int left = 0;
    int right = 0;

    for (int i = 0; i < arr.length; i++) {
        System.out.print(arr[i][i]);
        left += arr[i][i];
        right += arr[i][arr.length - (1 + i)];
    }

    return (Math.abs(left - right));
}
