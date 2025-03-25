from train2 import HashTable

h_t = HashTable.from_dict({'hola': 'hello',
                           98.6: 37,
                           False: True
                           })

print(h_t)
print(h_t.keys)
print(h_t.values)
print(h_t.pairs)
print(h_t.capacity)
print(h_t.load_factor)

print(h_t.pairs == list(zip(h_t.keys, h_t.values)))


