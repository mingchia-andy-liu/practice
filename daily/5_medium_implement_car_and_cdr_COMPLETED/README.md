# Medium

Asked by Jane Street.

## Question

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of `cons`:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`.

---

### Notes

### Questions to ask

1. what's the `f` function? are we implementing `f`?

### Workflow

* pair returns a function which will be called on the closure `a` and `b` variable.
* `f` is the **lambda** that operate on parameter `a` and `b`.

### Time

~ 15 mins

---

## Thoughts

* functional programming question.
* `f` is the function that `make a choice` which accepts 2 parameters `a` and `b`.
* for the interview question, we will make the `choice` of `first` or `last`

&nbsp;

* There is probably a follow question on this about function programming
* Interesting question
