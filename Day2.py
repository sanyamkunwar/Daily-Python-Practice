#Day 2

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result


print(multiply(1,2,3,4,5,6,7,8,9,10))
#================================================================================================

def save_user(**user):
    print(user)

save_user(id=1,name='John',age=22)

#================================================================================================

def fizz_buzz(input):
    if input%3==0 and input%5==0:
        return 'FizzBuzz'
    if input%3==0:
        return 'Fizz'
    if input%5==0:
        return 'Buzz'
    return input

print(fizz_buzz(15))

#================================================================================================

message = 'a'
def greet():
    global message
    message = 'b'

greet()
print(message)

#================================================================================================
