# Hard

Asked by Stripe.

## Question

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

`You can modify the input array in-place.`


---

### Notes

1. only positive, might be a trick there to use -infinity
1.

### Questions to ask

* what to return if all negative or 0

### Workflow

* sort them, find the missing O(nlogn)

* modifying the array in place sounds like a hint.

* create a window of lowest known and second known: 0, 0
* find the `max` and `min` <-- doesn't work if first missing is below the `min`
  * check the `min`
    * if it's `1`, then go down from `max`
    * if it's not, `1` return `1`.
* use a counter for current


### Analyze

* sort
  * time: O(nlogn)
  * space: O(n)

### Time

~ 40mins. Timeout.

---

### Internet

#### GeeksForFeeks

1. Naive approach: O(n^2)
1. Sorting: O(NlogN)
1. Hashing: O(N) on average. Build hash table of all positive elements, and find first missing one.


**Optimal**
##### O(n) time and O(1) extra space solution

> To mark presence of an element x, we change the value at the index x to negative

1. Get rid off negative and 0
1. Traverse the array and to mark presence of an element el, we change the sign of value at `index el` to negative.
    1. if it's out fo index, don't do anything.
1. We traverse the array again and print the first index which has positive value.
    1. Or all elements are negative, then return `size + 1`

```java
static int findMissingPositive(int arr[], int size) {
    int i;

    // Mark arr[i] as visited by making arr[arr[i] - 1] negative.
    // index is 0-based, so subtract 1.
    for(i = 0; i < size; i++) {
        int el = arr[i];

        // 1. check if it's in the bound
        // 2. check it haven't been visited
        if(el - 1 < size && arr[el - 1] > 0) {
            arr[el - 1] = -arr[el - 1];
        }
    }

    // Return the first index value at which
    // is positive
    for(i = 0; i < size; i++) {
        if (arr[i] > 0) {
            return i+1;  // index is 0-based
        }
    }

    return size+1;
}
```


---

## Thoughts

* Got the naive way and sorting way.
* Hash table is not terrible but if the value are huge, then the solution is bad, imo.
* Using array size as a trick to get the maximal number is need is creative.
*
