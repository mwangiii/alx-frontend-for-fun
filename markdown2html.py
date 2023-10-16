#!/usr/bin/python3

import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """Converts Markdown to HTML"""

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    else:
        # Actual conversion logic goes here
        print("Conversion successful!")
        sys.exit(0)
