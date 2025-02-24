/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (!head) return NULL;

    struct ListNode dummy; 
    dummy.next = head;  // Dummy node to handle edge cases
    struct ListNode* prev = &dummy;  // Pointer to track non-duplicate nodes

    while (head) {
        // Check if the current node has duplicates
        if (head->next && head->val == head->next->val) {
            // Skip all duplicate nodes
            while (head->next && head->val == head->next->val) {
                head = head->next;
            }
            prev->next = head->next;  // Remove duplicates
        } else {
            prev = prev->next;  // Move prev forward if no duplicates
        }
        head = head->next;  // Move to the next node
    }
    
    return dummy.next;
}