/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* current = head;

    while (current && current->next) {
        if (current->val == current->next->val) {
            struct ListNode* temp = current->next;  // Store duplicate node
            current->next = current->next->next;   // Skip the duplicate
            free(temp);  // Free memory
        } else {
            current = current->next;  // Move forward
        }
    }

        return head;
}