def main():
    a = int(input())
    b = int(input())
    operation = input()
    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == '/':
        print(a // b)

if __name__ == '__main__':
    main()