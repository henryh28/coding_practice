static String timeConversion(String s) {
    String hour = s.substring(0, 2);

    if (s.substring(s.length() - 2, s.length() - 1).equals("P")) {
        if (hour.equals("12")) {
            return (hour + s.substring(2, s.length() - 2));
        }

        int converted = Integer.valueOf(hour) + 12;
        return (String.valueOf(converted + s.substring(2, s.length() - 2)));
    } else {
        if (hour.equals("12")) {
            return ("00" + s.substring(2, s.length() -2));
        }

        return (s.substring(0, s.length() - 2));
    }
}


// ================ A python solution ==================
def timeConversion(s):
  if s[-2] == "P":
    hour = int(s[:2]) + 12
    converted = str(hour) + s[2:-2]

    return s[:-2] if s[:2] == "12" else converted
  else:
    return "00" + s[2:-2] if s[:2] == "12" else s[:-2]
