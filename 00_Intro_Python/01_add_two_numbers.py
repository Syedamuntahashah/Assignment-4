def main():
    
    num1: str = input("Enter first number: ")
    num1 = int(num1)
    num2: str = input("Enter second number: ")
    num2 = int(num2)
    total: int = num1 + num2
    result: int = total

    print("The sum of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()