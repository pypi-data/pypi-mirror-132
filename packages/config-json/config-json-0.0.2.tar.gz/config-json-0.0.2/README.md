# Config-Json
### An Easier Way to work with JSON configs
this library provide some top level method to make it easy to work with json
`Link: https://pypi.org/project/config-json/`
1. How to Use? 
```python
from jconf.config import Config

# u can either do
c = Config(config_name="main.json") # default name is main.json
# or
with Config(config_name="main.json")  as c:
    pass

```
2. functions available
```python
from jconf.config import Config

c = Config(config_name="main.json")
# returns all the keys from a json file
c.keys()
# returns all the values from a json file
c.values()
# gets the key from a json file
c.get('car')
# deletes a key from a json file
c.delete('car')
# update a value in a json file
c.update('car', 'tesla')
# sets a new key in json file
c.set('car2', 'ferari')
```
3. instead of using functions you can also use:
```python
from jconf.config import Config

c = Config('main.json')
# to/set or change a value
c['car'] = "name"
c['number_plate'] = ['3131', '3134', '3132']
# delete a key
del c['car']
# loop over a json file
for i in c:
    print(i) # returns a list of tuple with (key, value)
# updates / add to an existing key
c['car'] += {'model', 'year'}
# get a value
car = c['car']
```

* Automatically creates the passed config_name if it doesn't exists
