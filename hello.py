def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    n = int(input("put number: "))
    fib_sequence = fibonacci(n)
    print(f"Fibonacci: {fib_sequence}")

if __name__ == "__main__":
    main()


#i'm idiotasdfasdfasdf
#practicing for bug change