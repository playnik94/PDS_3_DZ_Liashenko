### https://tproger.ru/translations/demystifying-decorators-in-python


# def decorator_function(func):
#     def wrapper():
#         print('wrapper function!')
#         print(f'wrappered function {func}')
#         print('Execute wrappered function')
#         func()
#         print('Get out wrapper')
#     return wrapper
#
# @decorator_function
# def hello_world():
#     print('hellow_world')
#
# hello_world()



# def bencmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Время выполнение функции {end - start}")
#     return wrapper
#
# @bencmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#     print(webpage.status_code)
#
#
# fetch_webpage()

# def benchmark(func):
#     import time
#     def wrapper(*args, **kwargs):
#         stat = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print(f'Время выполнениея {end - stat} секунд')
#         return return_value
#     return wrapper
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return print(webpage.status_code)
#
# webpage = fetch_webpage('https://youtube.com')


# def benchmark(iter):
#     def actual_decorator(func):
#         import time
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iter):
#                 print(i)
#                 start = time.time()
#                 return_value = func(*args, **kwargs)
#                 end = time.time()
#                 total = total + (end-start)
#             print(f"Среднее время выполнения: {total/iter} секунд. ")
#             return return_value
#         return wrapper
#     return actual_decorator
#
# @benchmark(iter=10)
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return print(webpage.text[:100])
#
# web = fetch_webpage('https://google.com')

# from collections import deque
#
# class Memoized:
#     def __init__(self, cache_size=100):
#         self.cache_size = cache_size
#         self.call_args_queue = deque()
#         self.call_args_to_result = {}
#
#     def __call__(self, fn):
#         def new_func(*args, **kwargs):
#             memoization_key = self._convert_call_arguments_to_hash(args, kwargs)
#             if memoization_key not in self.call_args_to_result:
#                 result = fn(*args, **kwargs)
#                 self._update_cache_key_with_value(memoization_key, result)
#                 self._evict_cache_if_necessary()
#             return self.call_args_to_result[memoization_key]
#         return new_func
#
#     def _update_cache_key_with_value(self, key, value):
#         self.call_args_to_result[key] = value
#         self.call_args_queue.append(key)
#
#     def _evict_cache_if_necessary(self):
#         if len(self.call_args_queue) > self.cache_size:
#             oldest_key = self.call_args_queue.popleft()
#             del self.call_args_to_result[oldest_key]
#
#     @staticmethod
#     def _convert_call_arguments_to_hash(args, kwargs):
#         return hash(str(args) + str(kwargs))
#
#
# @Memoized(cache_size=5)
# def get_not_so_random_number_with_max(max_value):
#     import random
#     return print(random.random() * max_value)


# def second(iter):
#     def first(func):
#         from datetime import datetime
#         def wrapeer(*args, **kwargs):
#             for i in range(iter):
#                 start = datetime.now()
#                 return_value = func(*args, **kwargs)
#                 end = datetime.now()
#             print(f'Время выполнения фунции: {end-start} сукунд.')
#             return return_value
#         return wrapeer
#     return first
#
# @second(iter=10)
# def function(x):
#     return sum([abs(a - b) for a, b in zip(x, x[1:])])
#
# f = function(list(range(1, 1000000, 50)))
# print(f)

# def couter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step
#
# c1 = couter(10)
# c2 = couter()
#
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())

# def strip_string(string_chars=" "):
#     def do_strip(string):
#         return string.strip(string_chars)
#
#     return do_strip
#
# s = strip_string()
# s2 = strip_string(" !?/.,")
#
# print(s('hello..'))
# print(s2('hello.,!'))

# def yell(text):
#     return text.upper() + '!'
#
# bark = yell('hello')
#

#
# func = [bark, str.lower, str.capitalize]
# print(func)
#
# for f in func:
#     print(f,f('hey there'))
#
# print(func[0]('heyho'))

# def greet(func):
#     greeting = func('Hi i am a Python programer')
#     print(greeting)
#
# print(greet(yell))

# def whisper(text):
#     return text.lower() + ''
# print(greet(whisper))

# print(list(map(yell, ['hello', 'hey', 'hi'])))


# def speak(text):
#     def whisper(t):
#         return t.lower() + '___'
#     return whisper(text)

# print(speak('Hello World'))
# print(whisper('Yo'))

# def get_speak_func(text, volume):
#     def whisper():
#         return text.lower() + '...'
#     def yell():
#         return text.upper() + '...'
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper
#
# print(get_speak_func('Hellow World', 0.7)())
#
#
# def make_adder(n):
#     def add(x):
#         return x + n
#     return add
#
# plus3 = make_adder(3)
# plus5 = make_adder(5)
# print(plus3(4))
# print(plus5(4))
#
# class Adder:
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, x):
#         return self.n + x
#
# plus = Adder(3)
# print(plus(3))
#
# print(callable(plus))
# print(callable(make_adder))

########################
########################https://dbader.org/blog/python-first-class-functions
#########################
# def null_decorator(func):
#     return func
#
# def greet():
#     return print('Hello!')
#
# @null_decorator
# def greet():
#     return 'Hello!'
#
#
#
# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
# @uppercase
# def greet():
#     return 'hello'
#
#
#
#
# def strong(func):
#     def wrapper():
#         return 'Strong' + func() + 'Strong'
#     return wrapper
#
# def emphasis(func):
#     def wrapper():
#         return '<Emphasis>' + func() + '<Emphasis>'
#     return wrapper
# @strong
# @emphasis
# def greet():
#     return 'Python'
#
#
# def proxy(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @proxy
# def greet(name, main):
#     return f'name {name} ' + f'main {main}'
#
#
#
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace calling {func.__name__}()', f'with {args}, {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: {func.__name__}()', f'Returned {original_result}')
#         return original_result
#     return wrapper
# @trace
# def sey(name, line):
#     return f'name: {name} line: {line}'
#
#
# def greet():
#     '''Returned friendly greeting.'''
#     return 'Hello'
#
# decorated_greet = uppercase(greet)

# print(greet.__name__)
# print(greet.__doc__)
# print('\n')
# print(decorated_greet.__name__)
# print(decorated_greet.__doc__)

# import functools
#
# def uppercase(func):
#     import functools
#     @functools.wraps(func)
#     def wrapper():
#         return func().upper()
#     return wrapper
# @uppercase
# def greet():
#     """Return a friendly greeting."""
#     return 'nikita'
#
# print(greet())
#
# print(greet())
# print(greet.__name__)
# print(greet.__doc__)
# from functools import wraps
#

# def decoratdor_wraper(arg1, arg2):
#     def real_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return real_decorator
#
# @decoratdor_wraper(1, 2)
# def func():
#      ...
#
# print(func())
import cv2
from functools import wraps

# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         original_func = func(*args, **kwargs)
#         modifine_func = cv2.VideoCapture(original_func)
#         while True:
#             sucсess, img = modifine_func.read()
#             assert not isinstance(img, type(None)), 'image not found'
#             img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
#             cv2.imshow('gif', img)
#             if cv2.waitKey(15) & 0xff == ord('q'):
#                 break
#         return modifine_func
#     return  wrapper
#
# @decorator
# def call(a):
#     '''Function calling gif cat animation'''
#     return a
#
# print(call('D:/Neural_networks/Lesson_57/Aq.gif',))
# print(call.__doc__)
# print(call.__name__)

# from functools import wraps
#
# def decorator_wrapper(arg1, arg2):
#     def real_decorator(func): # объявляем декоратор
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#
#     return real_decorator     # возвращаем декоратор
#
#
# @decorator_wrapper(1, 2)
# def func():
#     ...
#
# print(func())
# from functools import wraps

# def add_mark(**kwargs):
#     def decorator(func):
#         for key, value in kwargs.items():
#             setattr(func, key, value)
#         return func
#     return decorator
#
# @add_mark(test=True, ordered=True)
# def test_function(a, b):
#     return a + b
#
# print(test_function(5, 6))
# print(test_function.ordered)
# print(test_function.test)
from  functools import wraps



# def restrict_args_type(required_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args):
#             if not all(isinstance(arg, required_type) for arg in args):
#                 raise ValueError(f'All arguments must be: {required_type.__name__}()')
#             return func(*args)
#         return wrapper
#     return decorator
#
# @restrict_args_type(int)
# def to_int(*args):
#     result = [bin(arg) for arg in args]
#     return result
#
# print(to_int(23, 1))
#
# restrict_args_type_str = restrict_args_type(str)
#
# @restrict_args_type_str
# def to_str(*args):
#     result = [arg.upper() for arg in args]
#     return result
#
# print(to_str('asdsf'))

# def restrict_args_type(required_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args):
#             if not all(isinstance(arg, required_type) for arg in args):
#                 raise ValueError(f'All arguments must be: {required_type.__name__}()')
#             return func(*args)
#         return wrapper
#     return decorator
#
# @restrict_args_type(int)
# def to_int(*args):
#     result = [bin(arg) for arg in args]
#     return result
#
# print(to_int(23, 1))

# def chekhing(type_date):
#     def first(func):
#         from datetime import datetime
#         def wrapper(*args):
#             start = datetime.now()
#             if not all(isinstance(arg, type_date) for arg in args):
#                 raise ValueError(f'All arguments must be {type_date}')
#             end = datetime.now()
#             print(f'time execution is: {end - start}')
#             return func(*args)
#         return wrapper
#     return first
#
# @chekhing(str)
# def upper_case(*args):
#     result = [s.upper() for s in args]
#     return result
#
# s = upper_case('nikita')
# print(s)
#
# @chekhing(int)
# def convert_ints(*args):
#     res = [bin(arg) for arg in args]
#     return res
#
# i = convert_ints(123, 3435)
# print(i)

# def first(requared_type):
#
#     def decore(func):
#
#         def wrapps(*args):
#
#             if not all(isinstance(arg, requared_type) for arg in args):
#                 raise TypeError(f'All arguments must be {requared_type}')
#             return func(*args)
#
#         return wrapps
#
#     return decore
#
# @first(int)
# def order(*args):
#     from datetime import datetime
#     start = datetime.now()
#     b = sorted(args)[::-1]
#     c = int(''.join(map(str, b)))
#     end = datetime.now()
#     print(f'Time is: {end - start}')
#     return c
#
# print(order(1237891087645))




