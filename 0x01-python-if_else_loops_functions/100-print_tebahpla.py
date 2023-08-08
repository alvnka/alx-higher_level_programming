#!/usr/bin/python3
for character in range(122, 96, -1):
    print("{}".format((chr(character)) if (character %
          2 == 0) else chr(character-32)), end='')
