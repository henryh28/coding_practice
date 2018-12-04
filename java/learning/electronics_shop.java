// ============= java solution ========================
static int getMoneySpent(int[] keyboards, int[] drives, int b) {
    int most = -1;
    int combined = 0;

    for (int i = 0; i < keyboards.length; i++) {
        for (int j = 0; j < drives.length; j++) {
            combined = keyboards[i] + drives[j];

            if (combined == b) {
                return (b);
            } else if (combined > most && combined < b) {
                most = combined;
            }
        }
    }
    return (most);
}

// ============= python equivalent ===================
def getMoneySpent(keyboards, drives, b):
    most = -1

    for keyboard in keyboards:
        for drive in drives:
            combined = keyboard + drive
            if combined == b:
                return b
            if combined > most and combined < b:
                most = keyboard + drive

    return most
