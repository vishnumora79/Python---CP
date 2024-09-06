# def apply(function,x):
#     return function(x)


# def function(x):
#     return x ** 2

# result = apply(function,5)

# print(result)


def my_decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")
    return wrapper
@my_decorator
def hi():
    print("Hello Everyone")    

hi()    