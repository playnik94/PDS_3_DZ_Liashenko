# hash_distribution.py
from collections import Counter
from string import printable


def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])


def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.pairs()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")


def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))


def hash_function2(text, t=None):
    if t is True:
        return type(text), sum(ord(character) for character in repr(text))

    return sum(ord(character) for character in repr(text))


def hash_function3(text, t=None):
    if t is True:
        return type(text), sum(index * ord(t) for index, t in enumerate(repr(text)))

    return sum(index * ord(t) for index, t in enumerate(repr(text)))




# p = 'python'
#
# print(hash_function(p))
# print(hash_function(p[::-1]))
# print('first')
# print(hash_function2(p, t=True))
# print(hash_function2(p[::-1], t=True))
# print('second')
# print(hash_function3(p, t=True))
# print(hash_function3(p[::-1], t=True))
# print('third')


def hash_functionn(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key).lstrip("'"), 1))


print(hash_functionn('python'))

# hash_functionn("a"), hash_functionn("b"), hash_functionn("c")
#
#
# plot(distribute(printable, 6, hash_functionn))


















# def hash_function(key):
#
#     return sum(ord(character) for character in str(key) )
#
#
# def hash_function2(text):
#
#     return sum(ord(character) for character in repr(text))
#
#
# def hash_f(num):
#     return sum(index * ord(n) for index, n in enumerate(repr(num), start=1))


# def hash_function(key):
#     return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))
#
#
# hash_function("a"), hash_function("b"), hash_function("c")
#
#
# def hash_function(key):
#     return sum(index * ord(character) for index, character in enumerate(repr(key).lstrip("'"), 1))
#
#
# hash_function("a"), hash_function("b"), hash_function("c")
#
#
# plot(distribute(printable, 6, hash_function))

