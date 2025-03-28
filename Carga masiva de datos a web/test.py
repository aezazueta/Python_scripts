def fibonacci(n):
    if n <= 0:
        print("Input should be positive integer")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Example usage:
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


