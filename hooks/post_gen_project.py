#!/usr/bin/env python
import os


def main():
    """Adds newlines back to every file, to make them PEP8 compliant."""
    root_path = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if path.endswith('.py'):
                with open(path, 'rb') as f:
                    contents = f.read()

                if not contents.endswith(b'\n'):
                    with open(path, 'wb') as f:
                        f.write((contents + b'\n').lstrip())


if __name__ == '__main__':
    main()
