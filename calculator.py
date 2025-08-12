
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: zero division error"
    return a / b

def main():
    print("=== Simple CLI Calculator ===")
    
    print("Type 'q' to quit\n")

    while True:
        expression = input("Enter expression: ").strip()

        if expression.lower() == 'q':
            print("Calculator closed.")
            break

        try:
            
            allowed_chars = "0123456789+-*/(). "
            if not all(char in allowed_chars for char in expression):
                print("Error: Invalid characters in expression.")
                continue

            result = eval(expression)  
            print(f"Result: {result}")

        except ZeroDivisionError:
            print("Error: zero division error")
        except Exception:
            print("Error: Invalid expression")

if __name__ == "__main__":
    main()
