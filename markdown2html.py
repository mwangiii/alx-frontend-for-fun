#!/usr/bin/python3

import sys
import os.path

if __name__ == '__main__':
    arg = sys.argv

    if len(arg) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = arg[1]
    output_file_name = arg[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
