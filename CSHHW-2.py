def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def main():
    while True:
        try:
            num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
            if num_terms <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Fibonacci series up to", num_terms, "terms:")
    print(fibonacci(num_terms))

if __name__ == "__main__":
    main()
