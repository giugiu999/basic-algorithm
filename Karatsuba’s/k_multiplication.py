#O(n^2)--> O(n^1.585)
def karatsuba(x, y):
    # base case
    if x < 10 or y < 10: 
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2 

    # Split x,y into 2parts
    high_x = x // 10**m
    low_x = x % 10**m
    high_y = y // 10**m
    low_y = y % 10**m

    # 3 varaible store value
    z2 = karatsuba(high_x, high_y)
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba(high_x + low_x, high_y + low_y)

    return z2 * 10**(2 * m) + (z1 - z2 - z0) * 10**m + z0

# testing
if __name__ == "__main__":
    num1 = 1234
    num2 = 5678
    result = karatsuba(num1, num2)
    print(f"Multiplication of {num1} and {num2} is: {result}")
