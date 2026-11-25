def remove_odd(number):
    result = []
    for num in number:
        if num % 2 == 0:
            result.append(num)
    return result

original = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
even_only = remove_odd(original)

print(f"Original list: {original}")
print(f"Cut-down list: {even_only}")