# Medium

Asked by Google.

## Question

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

---

### Notes

1. it's a binary tree
1.

### Questions to ask

* in what way to serialize it, any?


### Workflow

* BFS
* print it like `root|left,right|left.left,left.rigth,right.left,right.right`


### Analyze


### Time

---

## Thoughts

* harder than i thought it would be
* 0 gives a lot of trouble
* would never get bonus, though something close
