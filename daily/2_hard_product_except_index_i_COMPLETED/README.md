# Hard

Asked by Uber.

## Question

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

---

### Questions to ask

* while coding
  * what if the length is 0 or 1? return what?

### Workflow

* 1 pass to get the product, 1 pass to divide the product
* 0 or 0s really screw up the method
  * workaround:
    * if there are more than one 0s, return all 0 of size array
    * if there is one 0, then check if it's 0 during second pass
      * if so, use product, else use 0
    * if there is no 0, proceed as normal

### Analyze

* time: `O(n)` - 2 passes
* space: `O(1)` - constant except return array

### Time

~20 mins

---

## Bonus

Follow-up: what if you can't use division?

### Workflow

* use brute force
* `O(n^2)`

**INTERNET**
[stackoverflow](https://stackoverflow.com/a/2680697)

construct the 2 arrays like like
```
{              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
{ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
```

```java
int a[N] // This is the input
int products_below[N];
p=1;
for(int i=0;i<N;++i) {
  products_below[i]=p;
  p*=a[i];
}

int products_above[N];
p=1;
for(int i=N-1;i>=0;--i) {
  products_above[i]=p;
  p*=a[i];
}

int products[N]; // This is the result
for(int i=0;i<N;++i) {
  products[i]=products_below[i]*products_above[i];
}
```


### Time

N/A

---

## Thoughts

* harder than i thought it would be
* 0 gives a lot of trouble
* would never get bonus, though something close
