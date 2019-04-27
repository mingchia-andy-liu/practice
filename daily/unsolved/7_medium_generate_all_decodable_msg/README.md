# Medium

Asked by facebook.

## Question

Given the mapping `a = 1`, `b = 2`, ... `z = 26`, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

---

### Notes

- Sounds like a DP question: `give all`, `count all`, etc ...
- Sounds like the coin problem

### Questions to ask

### Workflow

- DP question: the smallest questions
  - 0 to 9 are the basic question since it's only 1 way to decode it.
- ~~2d array of solutions~~
  - ~~start with 1 char: find the way~~
  - ~~append 1 more char:~~
    - ~~find the way~~
    - ~~see if combine with last digits is less than 26.~~
    - ~~if so, add 1 more way~~

- top down
  - see if it's less than 26
    - if so, add 1 to the solution
    - split to recur(1) and recur(rest) / 2
  - but this will over counting the base
  - eg 111
    - 111 = 3
      - `1`, `11`: + 1 + 1 + (sub)/2 = 3
        - `1`, `1`: + 2
  - eg 2312
    - 2312 = 11
      - `2`, `312`: + 1 + 0 + (sub)/2 = 3.5
        - `3`, `12`: + 1 + 1 + (sub)/2 = 3
          - `1`, `2`: + 2
        - `31`, `2`: + 0 + 1 + (sub)/2 = 2
          - `3`, `1`: + 1 + 1
      - `23`, `12`: + 1 + 1 + (sub)/2 = 4
        - `2`, `3`, `1`, `2`: + 4
      - `231`, `2` + 0 + 1 + (sub)/2 = 3.5
        - `2`, `31`: + 1 + 0 + (sub)/2 = 2
          - `3`, `1`: + 2
        - `23`, `1`: + 2 + (sub)/2 = 3
          - `2`, `3`: + 2

- array of 26 ^ 26 solutions blocks
  -

### Analyze

### Time

~ 30 mins, give up

---

### Bonus

---

### Internet (for questions that are unsolved)

This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence. We initialize the total count of decodings as 0. We recur for two subproblems.
1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add the result to total count.

Following is the implementation of the above approach

---

### Thoughts
