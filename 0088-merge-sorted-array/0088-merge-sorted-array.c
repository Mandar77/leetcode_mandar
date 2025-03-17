void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;      // Last index of the initialized part of nums1
    int j = n - 1;      // Last index of nums2
    int k = m + n - 1;  // Last index of nums1 (including extra space)
    
    // Merge from the end to avoid overwriting elements in nums1
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
    
    // Copy any remaining elements from nums2 (if any)
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}