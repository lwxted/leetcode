/**
 * Definition for singly-linked list.
 * struct ListNode {
 *   int val;
 *   ListNode *next;
 *   ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <priority_queue>

typedef struct {
  bool operator() (const ListNode *l, const ListNode *r)
  {
    return l->val > r->val;
  }
} Comp;

class Solution {
public:
  ListNode *mergeKLists(vector<ListNode *>& lists) {
    priority_queue<ListNode *, std::vector<ListNode *>, Comp> pq;
    vector<ListNode *> nodes;
    for (int i = 0; i < lists.size(); ++i) {
      if (lists[i]) {
        pq.push(lists[i]);
      }
    }
    while (!pq.empty()) {
      ListNode *n = pq.top();
      nodes.push_back(n);
      pq.pop();
      if (n->next) {
        pq.push(n->next);
      }
    }
    if (nodes.empty()) {
      return NULL;
    }
    for (int i = 0; i < nodes.size() - 1; ++i) {
      nodes[i]->next = nodes[i + 1];
    }
    nodes[nodes.size() - 1]->next = NULL;
    return nodes[0];
  }
};
