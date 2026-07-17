import sys

def hello(x):
    print(f'Hello, {x}!')

if __name__ == '__main__':
    hello(f'installing {sys.argv[1] if len(sys.argv) > 1 else None}..')

