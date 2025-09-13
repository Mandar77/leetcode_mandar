bool isPalindrome(int x) {
    long reverse = 0;
    int y = x;
    if(x<0)
    {
        return false;
    }
    while (y>0)
    {
        reverse = reverse * 10 + y % 10;
        y = y/10;
    }
    return reverse == x;
}
