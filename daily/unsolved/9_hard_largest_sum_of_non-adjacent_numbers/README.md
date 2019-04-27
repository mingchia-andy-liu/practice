# Hard

Asked by **Airbnb**.

## Question

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or `negative`.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

---

### Notes

- Can be `0` or `negative`

### Questions to ask

### Workflow

- Brute force
  - pick 1 number match with (N - 1 - 1) numbers
  - O(N^2)

- Dynamic Programming
  - not really
  - how to merge sub problems?

- Brute force is *WRONG* because we need to compare which combination is optimal

### Analyze

### Time

- Give up
- 15 mins: no clue how to solve it.

---

### Bonus

Can you do this in O(N) time and constant space?

---

&nbsp;

&nbsp;

&nbsp;

### Internet (for questions that are unsolved)

**CHEATED From GeeksForGeeks**


Algorithm:
Loop for all elements in arr[] and maintain two sums `incl` and `excl` where `incl` = Max sum including the previous element and `excl` = Max sum excluding the previous element.

---

### Thoughts

- the algo seems easy, still doesn't understand the algo
- using curr max and new max seems like a method to find the local max/min questions

