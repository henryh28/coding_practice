// ================ java solution ======================
static int howManyGames(int p, int d, int m, int s) {
    if (s < p) {
        return 0;
    }

    int answer = 0;
    List<Integer> prices = new ArrayList();

    for (int i = p; i > m ; i -= d) {
        prices.add(i);
    }
    prices.add(m);

    while (s >= prices.get(0)) {
        s -= prices.size() > 1 ? prices.remove(0) : prices.get(0);
        answer += 1;
    }

    return (answer);
}

// ================ python solution ======================
def howManyGames(p, d, m, s):
    if s < p:
        return 0

    answer = 0
    prices = [cost for cost in range(p, m, -d)]
    prices.append(m)

    while s >= prices[0]:
        s -= prices.pop(0) if len(prices) > 1 else prices[0]
        answer += 1

    return (answer)
    
