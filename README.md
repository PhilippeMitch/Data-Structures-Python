## Data Structures With Python

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

---
Create a function to return a list of names from the json file [people.json](https://github.com/Fictizia/Master-en-Big-Data-y-Machine-Learning_ed1/blob/master/capitulo_2/resources/people.json), matchings
both the provided birth year and specified gender.


**Load the data**\
json is a package encoding and decoding JSON data
The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
```python
import json
```
```python
with open('people.json') as d:
  data = json.load(d)
```
We want to have the name of a person with the keys birth_year and gender
```python
def get(birth_year, gender, db = data):
  return [i for i in db if (i['birth_year'] == birth_year and i['gender'] == gender)][0]['name']
 ```
 ```python
 print(get("24BBY", "male"))
 ```
Biggs Darklighter
