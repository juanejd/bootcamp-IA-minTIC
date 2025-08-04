# Commands to use

```bash
python --version
pip list
```

# create virtual environment

```bash
python -m venv venv
```

# activate virtual environment

```bash
source venv/bin/activate
```

## Data structure in pandas

| Data Structure | Description                            |
| -------------- | -------------------------------------- |
| Series         | 1D array                               |
| DataFrame      | 2D array                               |
| Panel          | Similary to a dictionary of DataFrames |

## creation of series

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
print(s)
```

# manage git

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourrepository.git
git push -u origin main
```
