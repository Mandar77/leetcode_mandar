int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

bool hasGroupsSizeX(int* deck, int deckSize) {
    if (deckSize < 2) return false;

    int count[MAX_CANON + 1] = {0};  // Frequency array for card values

    // Count occurrences of each card
    for (int i = 0; i < deckSize; i++) {
        count[deck[i]]++;
    }

    // Compute GCD of all non-zero frequencies
    int commonGCD = 0;
    for (int i = 0; i <= MAX_CANON; i++) {
        if (count[i] > 0) {
            if (commonGCD == 0)
                commonGCD = count[i];
            else
                commonGCD = gcd(commonGCD, count[i]);
        }
    }

    return commonGCD >= 2;
}