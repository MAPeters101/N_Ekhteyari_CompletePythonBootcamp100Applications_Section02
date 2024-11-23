"""
text :      str         x = "hello World

numbers :   int         x = 20
            float       x = 20.4
            complex     x = 1j

sequence :  list        x = ['apple', 2, 'banana']
            tuple       x = (1, 2, 3, 4, 'name')
            range       x = range(4)

mapping :   dict        x = {'name': 'Mark', 'age': 25}

set :       set         x = {1, 2, 3, 4}
            frozenset   x = frozenset({'apple', 'cherry'})

boolean :   bool        x = True

binary :    bytes       x = b"hello"
            bytearray   x = bytearray(5)
            memoryview  x = memoryview(bytes(6))

none :      None

"""

x = {'name': 'Mark', 'age': 25}
print(x)
print(type(x))
print()


x = ['apple', 2, 'banana']
print(x)
print(type(x))
print()

x = False
print(x)
print(type(x))
print()


x = b"hello"
print(x)
print(type(x))
print()

x = bytearray(5)
print(x)
print(type(x))
print()

x = memoryview(bytes(6))
print(x)
print(type(x))
print()

x = None
print(x)
print(type(x))
print()






