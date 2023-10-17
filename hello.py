# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    """Returns the full name with proper capitalization."""
    names = [name.capitalize() for name in (first_name, last_name) if name]
    return " ".join(names)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # => ['hello.py']
        print(f'Hello{full_name("", "")}!')
    elif len(sys.argv) == 2:
        # => ['hello.py', 'John' ]
        print(f'Hello {full_name(sys.argv[1], "")}!')
    else:
        # => ['hello.py', 'John', 'Lennon']
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}!")
