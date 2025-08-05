# Introduction to Pandas

## Creation of series objects

```python
height = {"Santiago": 180, "Pedro": 170, "Juan": 160, "Maria": 150, "Ana": 140}
result = pd.Series(height)

print(result)
print()
# Serie object creation inizialized with a scalar

s = pd.Series(34, ["test1", "test2", "test3"])
print(s)
```
