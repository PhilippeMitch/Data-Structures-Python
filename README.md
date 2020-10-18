## Data Structures Python

Given a list of strings, find the **3 most common stringhs** and their **count**. 

Implement a function that for a list of strings return a list (at maximum) 3 tuples containing:
*  The stringh(s) **lengh**
*  The number of occurences of strings of that lengh

**Counter** is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
```python 
from collections import Counter
```

```python
a = ["Fiat", "Ford", "Jeep", "Cadillac", "Jaguar", "Subaru"]
print(Counter(map(len, a)))
```

Counter({4: 3, 6: 2, 8: 1})
