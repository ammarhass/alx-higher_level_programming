#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    Sum = 0
    for i in range(length):
        Sum += int(sys.argv[i + 1])
    print("{}".format(Sum))
