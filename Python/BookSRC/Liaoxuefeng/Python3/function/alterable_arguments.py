# Calculate 1 + 2*2 + 3*3 + ...
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    
print(calc())
print(calc(1,2))

nums = [1,2,3]
print(calc(*nums))