# Dictionary examples
my_dict = {"key1": 123, "key2": "value2", 'key3': {"123": [1, 2, 'grabme']}}
print(my_dict['key3']['123'][2].upper())

dict2 = {'lunch': 'pizza', 'bfast': 'eggs'}
print(dict2['lunch'])

dict2['lunch'] = 'burger'
print(dict2['lunch'])
