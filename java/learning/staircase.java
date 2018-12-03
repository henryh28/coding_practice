// Complete the staircase function below (done with string builder).
static void staircase(int n) {

    StringBuilder filler = new StringBuilder();

    for (int i = 0; i < n; i++) {
        filler.append(" ");
    }

    for (int i = 1; i <= n; i++) {
        filler.replace(filler.length() - i, filler.length() - (i - 1), "#");
        System.out.println(filler);
    }
}

// Complete the staircase function below. (done with array)
static void staircase(int n) {

    char[] line = new char[n];
    Arrays.fill(line, ' ');

    for (int i = 1; i <= n; i++) {
        line[n-i] = '#';
        System.out.println(line);
    }
}
