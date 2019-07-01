# Array

## Table of Content
* [Fundamental](#fundamental)
* [Run time](#run-time)
* [Create an array](#create-an-array)
  + [N-dimension array](#n-dimension-array)
* [Loops](#loops)
  + [for each](#for-each)
* [Array Methods](#array-methods)
  + [AsList](#aslist)
  + [Equals](#equals)
  + [Sorts](#sorts)
    - [Ascending order](#ascending-order)
    - [Descending order](#descending-order)
    - [Custom sort](#custom-sort)
    - [Arrays.sort() vs Collections.sort()](#arrayssort-vs-collectionssort)
* [Common Problems](#common-problems)
  + [Reverse](#reverse)
  + [Contains](#contains)
  + [Has Duplicates](#has-duplicates)
  + [Pivot/Partition](#pivot-partition)


## Fundamental
```java
int[] A = new int[10];  // references to the array;

System.out.println(A); // base address: ie. [I@de0a01f

A[0] = 123;
System.out.println(A[0]); // 123
```

## Run time
```java
// Get
X = A[i] // O(1)

// Set
A[i] = X; // O(1)

// Remove
delete A[i] // O(N - index)

// Size
A.length // O(1)
```

## Create an array

Declare an array.
``` java
// type arrayRefVar = new dataType[arraySize];
int[] intArray = new int[10];
```

Declare an array with init values
```java
// dataType[] arrayRefVar = {value0, value1, ..., valuek};
int[] intArray = {1, 2, 3, 4, 5};
// intArray -> [1, 2, 3, 4, 5]
```

### N-dimension array

```java
// dataType[1st dimension][2nd dimension][]..[Nth dimension] arrayRefVar = new dataType[size1][size2]….[sizeN];
int[][] 2dArray = new int[10][5];
// this is a 10 by 5 matrix;

int[][][] 3dArray = new int[10][5][2];
// this is a 10 by 5 by 2 cube;
```

## Loops

```java
int[] arr = new int[10];
for (int i = 0; i < arr.length; i++) {
  System.out.println(arr[i]);
}
```

### for each
```java
int[] nums = {1, 2, 3, 4, 5};
for (int num: nums) {
  System.out.println(num + ", ");
}
// outputs: 1, 2, 3, 4, 5
```

## Array Methods

package
```java
import java.utils.Arrays
```

### AsList

```java
Integer[] A =  {1, 2, 3, 4, 5};
List<Integer> list = Arrays.asList(A);
```

_**NOTE**_

There's no such thing as a `List<int>` in Java - `generics` don't support primitives.

`Autoboxing` only happens for a **SINGLE** element, not for arrays of primitives.

```java
int[] A = {1, 2, 3, 4, 5};

// the list created will be List<int[]>
// NOT List<Integer>
List badList = Arrays.asList(A);

// returns 1 instead of 5
System.out.print(badList.size());
// prints 3
System.out.print(badList.get(0)[2]);


// how to fix it in **Java 8**
Integer[] boxedIntArray = Arrays.stream(A).boxed().toArray(Integer[]::new);
List<Integer> boxedIntList = Arrays.stream(A).boxed().collect(Collectors.toList());
```

### Equals

```java
// Equals (array1, array2): This method checks if both the arrays are equal or not.
int[] A = {1, 2, 3, 4};
int[] B = {1, 2, 3, 4};

Arrays.equals(A, B); // true
```

### Sorts

#### Ascending order
```java
public static sort(T[] arr, int from_Index, int to_Index)
```

```java
import java.utils.Arrays;

int[] A = {5, 4, 3, 6, 5, 0, 7, 9};

// sorts the array in place.
Arrays.sort(A);
// [0, 3, 4, 5, 5, 6, 7, 9]
System.out.print(Arrays.toString(A));

// sorts with range.
Arrays.sort(A, 3, 7);
// [5, 4, 3, 0, 5, 6, 7, 9]
System.out.print(Arrays.toString(A));
```

#### Descending order
```java
import java.util.Arrays;
import java.util.Collections;

int[] A = {13, 7, 6, 45, 21, 9, 2, 100};

// sorts A[] in descending order
Arrays.sort(A, Collections.reverseOrder());

// A -> [100, 45, 21, 13, 9, 7, 6, 2]
```

#### Custom sort
Implements the `Comparator<T>` interface.

```java
import java.util.Arrays;
import java.util.Comparator;

class Score {
    public int score;
    public Score(int score) { this.score = score; }
}

Score[] scores = {
  new Score(10),
  new Score(5),
  new Score(8),
  new Score(0)
};

Arrays.sorts(Scores, new Comparator<Score>() {
  public int compare(Score s1, Score s2) {
    return s1 - s2; // ascending
  }
})

// scores -> [0, 5, 7, 10] (in terms of Score)
```

Use `lambda`

```java
Integer[] A = {5, 4, 3, 6, 5, 0, 7, 9};

// The complier deduces the type from context, using process known as "Type interface"
Arrays.sort(A, (n1, n2) -> (n1 - n2));

System.out.println(Arrays.toString(A));
// A -> [0, 3, 4, 5, 5, 6, 7, 9]
```

#### Arrays.sort() vs Collections.sort()
`Arrays.sort` works for arrays which can be of primitive data type also. `Collections.sort()` works for objects `Collections` like `ArrayList`, `LinkedList`, etc.

## Common Problems
### Reverse

`Arrays` class in Java doesn’t have reverse method. We can use `Collections.reverse()` to reverse an array also.

```java
import java.util.Arrays;
import java.util.Collections;

int arr[] = {10, 20, 30, 40, 50};

Collections.reverse(Arrays.asList(arr));

// [50, 40, 30, 20, 10]
System.out.println(Arrays.toString(arr));
```

### Contains

Simple loops
```java
Integer[] A = {1, 2, 3, 4, 5};
for (int i = 0; i < A.length; i++) {
  if (A[i].equals(target)) {
    return true;
  }
  return false;
}
```

Use list
```java
Integer[] A = {1, 2, 3, 4, 5};
return Array.asList(A).contains(target);
```

Use set

```java
Integer[] A = {1, 2, 3, 4, 5};
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(A));
return set.contains(target);
```

### Has Duplicates

Return `true` or `false`.

Use Set

```java
Integer[] A = {1, 2, 3, 4, 5};
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(A));

// because set does not allow duplicates, the size will be different.
return set.size() != A.length;
```

### Finds Duplicates

Use set / map

```java
int[] nums = {1,2,2,3,4,5,5,6,7,7,8,9};

List<Integer> dups = new ArrayList<Integer>();
HashSet<Integer> set = new HashSet<Integer>();
for (int num: nums) {
  if (!set.add(num)) {
    dups.add(num);
  }
}
```

### Find Non-Duplicate

Use `XOR` mask. If everything has 2 occurrences, only 1 number has 1 occurrence.

```java
int[] nums = {1,1,2,2,3,3,4,4,5};

// use the first element as starting
int mask = nums[0];
for (int num: nums) {
  mask ^= num;
}

// Mask will be the non-duplicated value.
System.out.println(mask); // 5
```

### Pivot/Partition

Useful for quick sort.

```java
// Pivot over the value
public int pivot(int[] arr, int pivotValue) {
  // size of the sub-array that is value less than pivot
  int size = 0;
  for (int i = 0; i < arr.length; i++) {
    if (arr[i] < pivotValue) {
      // put the current value on the LEFT side of pivot
      swap(arr, i, size);

      // increase pivot pointer
      size++;
    }
  }
  return size;
}

// Pivot over an index
public int pivotIndex(int[] arr, int index) {
  int size = 0;
  int pivot = arr[index];
  swap(arr, 0, index);
  // start at index 1 because 0 is the pivot
  for (int i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      swap(arr, i, size);
      size++;
    }
  }
  // put the pivot back in the pivot index
  swap(arr, 0, size - 1);
  return size;
}
```

Example

```java
int[] A = {-5, 2, 9, -4, 7, 19, -8, 11, 4, 6, 9};
int pivotIndex = pivot(A, 0);
// A -> [-5, -4, -8, 2, 7, 19, 9, 11, 4, 6, 9]
// pivotIndex -> 3, A[pivotIndex] = 2
```


### Merge

Useful for merge sort

```java
public int[] merge(int[] a, int[] b) {
  int[] res = new int[a.length + b.length];

  int aIdx = 0;
  int bIdx = 0;

  int curr = 0;
  while (aIdx < a.length && bIdx < b.length) {
    if (a[aIdx] < b[bIdx]) {
      res[curr++] = a[aIdx++];
    } else {
      res[curr++] = b[bIdx++];
    }
  }
  while (aIdx < a.length) {
      res[curr++] = a[aIdx++];
  }
  while (bIdx < b.length) {
      res[curr++] = b[bIdx++];
  }

  return res;
}
```

Example

```java
int[] A = {-10,-1,0,1,1,1,5,6,12,30};
int[] B = {-50,-23,-10,-2,0,0,5,7,9};
int[] C = merge(A, B);

// [ -50, -23, -10, -10, -2, -1, 0, 0, 0, 1, 1, 1, 5, 5, 6, 7, 9, 12, 30 ]
System.out.println(Arrays.toString(C));
```
