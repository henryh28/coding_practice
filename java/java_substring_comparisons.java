public static String getSmallestAndLargest(String s, int k) {
    String smallest = "";
    String largest = "";
    smallest = s.substring(0, k);

    for (int i = 0; i <= s.length() - k; i++) {
      String chunk = s.substring(i, i + k);

      if (chunk.compareTo(smallest) < 0) { smallest = chunk; }
      if (chunk.compareTo(largest) > 0) { largest = chunk; }
    }
  return (smallest + "\n" + largest);
}
