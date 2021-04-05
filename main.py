import sys
sys.path.insert(1, './Division-with-remainder')
import func

def main():
    try:
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
            print(a / b)
        elif operation == '%':
            print(func.func(a, b))
        else:
            raise ValueError
    except ValueError:
        print('Enter two integers, each on a new line, then enter the operation character on the next line(\'+\', \'-\', \'*\', \'/\'')

if __name__ == '__main__':
    main()