// Answer in java
// Complete the birthdayCakeCandles function below.
static int birthdayCakeCandles(int[] ar) {
    int answer = 0;
    int max = Arrays.stream(ar).max().getAsInt();

    for (int i = 0; i < ar.length; i++) {
        if (ar[i] == max) {
            answer += 1;
        }
    }

    return (answer);
}

// =========== Answer in python =============
def birthdayCakeCandles(ar):
  return (ar.count(max(ar)))
  
