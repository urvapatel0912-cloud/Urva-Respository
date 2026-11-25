from traceback import print_tb


def list_sum(number):
    total = 0
    for num in number:
        total += num
    return total

my_list = [23,9,15,9,23,10,34]
result = list_sum(my_list)
print(f"List of integers: {my_list}")
print(f"Sum of integers: {result}")