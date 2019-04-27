
#Hard

Asked by Google.

## Question

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

---
&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;



### Notes

### Questions to ask

### Workflow

- how do you decode `1` or `0`?
-

### Analyze

### Time

- 10mins, give up



### Internet (for questions that are unsolved)

```
--> refers to a pointer

--> NODE A <--> NODE B <--> NODE C <--> NODE D --> null
```

- Trick IMO,
  - start the list with `0`s `XOR` address of `A`.
  - need to know the address of previous node

- Node A's `both` = `0 XOR address(A)`
- Node B's `both` = `address(A) XOR address(B)`
- Node C's `both` = `address(C) XOR address(D)`
- Node D's `both` = `address(D) XOR 0`

- We can traverse the XOR list in both forward and reverse direction. While traversing the list we need to remember the address of the previously accessed node in order to calculate the next node’s address. For example when we are at node C, we must have address of B. XOR of add(B) and npx of C gives us the add(D). The reason is simple: npx(C) is “add(B) XOR add(D)”. If we do xor of npx(C) with add(B), we get the result as “add(B) XOR add(D) XOR add(B)” which is “add(D) XOR 0” which is “add(D)”. So we have the address of next node. Similarly we can traverse the list in backward direction.

---

### Thoughts
