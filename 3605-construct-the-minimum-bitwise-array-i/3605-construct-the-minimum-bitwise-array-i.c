/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* ans = (int*)malloc(numsSize * sizeof(int));

    if (!ans) return NULL;
    for(int i = 0; i < numsSize; i++){
        int num = nums[i];
        if (num == 2){
            ans[i] = -1;
        }
        else {
            int a = num;
            int bit = 1;
            while(a&bit){
                bit <<= 1;
            }
            ans[i] = num ^ (bit >> 1);
        }
    }
    return ans;
}