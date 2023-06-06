#Dictionary is a data structure that stores key-value pairs.

myDictionary = {
    "apple" : 100,
    "banana" : 200,
    "melon" : 300
}

type(myDictionary) # dict

myDictionary["apple"] # 100

myDictionary["melon"] = 400 # {"apple" : 100, "banana" : 200, "melon" : 400}
myDictionary["orange"] = 500 # {"apple" : 100, "banana" : 200, "melon" : 400, "orange" : 500}

myDictionary.keys() # dict_keys(['apple', 'banana', 'melon', 'orange'])
myDictionary.values() # dict_values([100, 200, 400, 500])
myDictionary.items() # dict_items([('apple', 100), ('banana', 200), ('melon', 400), ('orange', 500)])
myDictionary.get("apple") # 100
myDictionary.get("apple", 0) # 100
myDictionary.get("pineapple", 0) # 0
myDictionary.pop("apple") # 100
myDictionary # {'banana': 200, 'melon': 400, 'orange': 500}

myOtherDictionary = {
    "a": 100,
    "b": [1,2,3],
    "c": True
}

myOtherDictionary["b"] # [1,2,3]
myOtherDictionary["b"][1] # 2
