int mySqrt(int x) {
    if (x == 0 || x == 1) return x;

    int low = 0, high = x/2, result = 0;
    while (low <= high) {
        long mid = low + (high - low) / 2;

        long square = mid * mid;
        if (square == x) return mid;
        if (square < x) {
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}