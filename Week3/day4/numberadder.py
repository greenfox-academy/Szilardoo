# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def count_down(number):
    if number == 0:
        return 0
    else:
        return number + count_down(number-1)

print(count_down(6))
