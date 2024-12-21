def check(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a, b):
   return (a / b)

print(div(6,2))
print(div(6,0))


