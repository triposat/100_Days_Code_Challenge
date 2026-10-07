fib:
```
 for _ in range(n):
        print(a)
        a, b = b, a + b
```

* Python evaluates the right-hand side before assigning either variable, so a + b uses both old values.
