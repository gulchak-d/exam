import sys

def fibonacci(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("має бути ціле ЧИСЛО")

    if n < 0:
        raise ValueError("число має бути більше або рівне 0")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    try:
        user_input = input("введіть (n): ")
        result = fibonacci(user_input)
        print(f"значення {user_input}-го елемента Фібоначчі: {result}")
    except Exception as e:
        print(f"ерор: {e}")
        sys.exit(1)
