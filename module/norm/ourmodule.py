import sys

def square(x):
    print(x**2)

def hello(x):
    print(f'Hello, {x}!')

if __name__ == '__main__':
    hello(f'installing {sys.argv[1] if len(sys.argv) > 1 else None}..')

