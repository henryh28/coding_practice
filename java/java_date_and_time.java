import java.util.*;

public class Solution {
  public static String getDay(String day, String month, String year) {
    Calendar gregorian = Calendar.getInstance();
    gregorian.set(Integer.valueOf(year), (Integer.valueOf(month) - 1), Integer.valueOf(day));
    
    return gregorian.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.getDefault()).toUpperCase();
  }
