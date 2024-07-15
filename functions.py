def call_numbers():
    for number in range(0, 10):
        print(number)


lista = range(0, 10)


def call_numbers_with_limit(limit):

    for number in range(limit):
        print(number)


call_numbers_with_limit(50)


def calculator(x=10, y=15):
    #print(x-y)
    return x-y


calculator(x=20, y=12)
calculator()
calculator(5)

result = calculator(5)
print("Result is", result)
