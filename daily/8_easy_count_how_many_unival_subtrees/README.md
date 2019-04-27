# Easy

Asked by **Google**.

## Question

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example this tree has 5 unival subtrees.
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

---

### Notes

- Binary tree
- Recursion

### Workflow

- Count left's unival subtree
- Count right's unival subtree
- Check if itself is a unival tree, if so, add to count

- Add all 3

- **FORGOT** to count leaf as a tree

### Analyze

- FORGOT to count leaf which was stupid
- O(N) because needs to traverse all node

### Time

- Total: 17 mins (including writing `Node` class and test cases)
- Code: ~10 mins to complete

---

### Thoughts

- Easy question took too long to finish
- Writing out the `Node` class also too long
- Unfamiliar with python check `null` values
