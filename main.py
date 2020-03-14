#!/usr/bin/python3
import sys

class CharacterMapping:
    def checkMapping(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 != len2:
            return False

        len1Unique = len(set(s1))
        if len1Unique < len1:
            return False

        return True

def main():
    if len(sys.argv) != 3:
        print('Invalid input: argument missing')
        return
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    mapping = CharacterMapping()
    if mapping.checkMapping(s1, s2):
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    main()