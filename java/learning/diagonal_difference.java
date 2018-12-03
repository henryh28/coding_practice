// Complete the diagonalDifference function below.
static int diagonalDifference(int[][] arr) {
    int left = 0;
    int right = 0;

    for (int i = 0; i < arr.length; i++) {
        left += arr[i][i];
        right += arr[i][arr.length - (1 + i)];
    }

    return (Math.abs(left - right));
}


// =============== A python solution =============
def diagonalDifference(arr):
    left, right = 0, 0

    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][-(1 + i)]
    
    return abs(left - right)
