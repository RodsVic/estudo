from decorator import my_decorator, uppercase_decorator, split_string

# Exemplo 1
@my_decorator
def my_function():
    print("Dentro da função")

my_function()

# Exemplo 2
@uppercase_decorator
def text():
    return "Hello World"

print(text())

# Exemplo 3
@split_string
def example():
    return "Apendendo Python e criando decorators"

print(example())