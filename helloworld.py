# helloworld.py
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python helloworld.py <name>")
    else:
        name = sys.argv[1]
        print("Hello, " + name + "!")


if __name__ == "__main__":
    main()
