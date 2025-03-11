int getSumOfSquares(int n) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    for (int i = 0; i < 100; i++) {  // Arbitrary upper limit to avoid infinite loops
        if (n == 1) return true;
        n = getSumOfSquares(n);
    }
    return false;
}