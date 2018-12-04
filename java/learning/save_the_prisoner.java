// ========== java  solution ==========

static int saveThePrisoner(int n, int m, int s) {
    int answer = Math.max(0, (m + s - 1) % n);

    return (answer != 0 ? answer : n);
}

// ========== python solution ==========
def saveThePrisoner(n, m, s):
    answer = max(0, (m + s - 1) % n)

    return (answer if answer else n)
    
