#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) != 3:
        print('Invalid input: argument missing')
        return
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    len1 = len(s1)
    len2 = len(s2)
    if len1 != len2:
        print('false')
        return
    len1Unique = len(set(s1))

    if len1Unique < len1:
        print('false')
        return
    print('true')

if __name__ == "__main__":
    main()