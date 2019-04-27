# Easy

Asked by Google.

## Question

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [4, 10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

---

### Questions to ask

1. Do i need to return the keys
1. Are there any duplicates?
1. Are there any negatives?
1. Is the array sorted? (does not really help)

### Workflow

* Use a hash table to create "mismatch" buckets. First pass.
* Use the elements in the array to look key in the table. Second pass.

### Time

~ 15 mins

---

## Bonus

Can you do this in one pass?

### Workflow

* only need to return true/false
* use 2 buckets: ADD and MINUS
  * ADD:
    * Actual elements
    * purpose: matching with the current "diff" with all previous actual elements
  * MINUS:
    * Diff from previous elements
    * purpose: matching current element with all previous "diff"s

```python
for element in arr:
  diff = k - element
  if (diff in add):       return True
  if (element in minus):  return True
  minus[diff] = True
  add[element] = True
return False
```

### Time

~ 20 mins


---

## Thoughts

* For bonus, write out what's actually in the array
* what's the purpose for each array
