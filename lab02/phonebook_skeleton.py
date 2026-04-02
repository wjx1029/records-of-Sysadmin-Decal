#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'a') as f:
            f.write(f"{sys.argv[2]}+{sys.argv[-1]}\n")

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES, 'r') as file:
                for line in file:
                    name, phone_num = line.strip().split("+")
                    print(f'{name} {phone_num}')
    
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r') as file:
            for line in file:
                name, phone_num = line.strip().split("+")
                if name == sys.argv[2]:
                    print(phone_num)

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line for line in lines if name not in line]
    

        with open(PHONEBOOK_ENTRIES, 'w', encoding='utf-8') as file:

            file.writelines(lines)

    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        open(PHONEBOOK_ENTRIES, 'w').close()

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            # YOUR CODE HERE #


if __name__ == "__main__":
    main()
