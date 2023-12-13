def print_fibonacci(length):
    fib_sequence = [0, 1]
    for _ in range(2, length):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    print(fib_sequence[:length])
