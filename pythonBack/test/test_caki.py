from assistants import *
from grazie_utils import grazie_assistant_request

tekst_zadatka=" You are given two non-empty linked lists" \
              " representing two non-negative integers. The digits are stored in reverse order," \
              " and each of their nodes contains a single digit. Add the two numbers and return the" \
              " sum as a linked list.You may assume the two numbers do not contain any leading zero," \
              " except the number 0 itself."



pokusaj_resenja = "/** \
 * Definition for singly-linked list. \
 * struct ListNode { \
 *     int val; \
 *     ListNode *next; \
 *     ListNode() : val(0), next(nullptr) {} \
 *     ListNode(int x) : val(x), next(nullptr) {} \
 *     ListNode(int x, ListNode *next) : val(x), next(next) {} \
 * }; \
 */ " + """
 class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* p = l1, * q = l2, * curr = dummyHead;
        int carry = 0;
        while (p != nullptr || q != nullptr) {
            int x = (p != nullptr) ? p->val : 0;
            int y = (q != nullptr) ? q->val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            if (p != nullptr) p = p->next;
            if (q != nullptr) q = q->next;
        }
        if (carry > 0) {
            curr->next = new ListNode(carry);
        }
        return dummyHead->next;
    }
};"""


vesna = Vesna()
luka = Luka()
vid = Vid()
veles = Veles()
vlada = CodeValidator()


print("Hintuje Vlada")
grazie_assistant_request(vlada, tekst_zadatka, "", pokusaj_resenja)

print("Hintuje Luka")
grazie_assistant_request(luka, tekst_zadatka, "", pokusaj_resenja)
print("Hintuje Vesna")
grazie_assistant_request(vesna, tekst_zadatka, "", pokusaj_resenja)
print("Hintuje Vid")
grazie_assistant_request(vid, tekst_zadatka, "", pokusaj_resenja)
print("Hintuje Veles")
grazie_assistant_request(veles, tekst_zadatka, "", pokusaj_resenja)
