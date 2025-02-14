/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int* returnSize, int** returnColumnSizes) {
    *returnSize = numRows;
    
    // Allocate memory for row sizes
    *returnColumnSizes = (int*)malloc(numRows * sizeof(int));
    
    // Allocate memory for the 2D triangle
    int** triangle = (int**)malloc(numRows * sizeof(int*));

    for (int i = 0; i < numRows; i++) {
        (*returnColumnSizes)[i] = i + 1;  // Number of elements in each row
        triangle[i] = (int*)malloc((i + 1) * sizeof(int));

        triangle[i][0] = 1;  // First element is always 1
        triangle[i][i] = 1;  // Last element is always 1

        // Compute middle elements
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    return triangle;
}