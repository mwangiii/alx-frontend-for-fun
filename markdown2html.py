#!/usr/bin/python3

""" a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
"""
import sys
import os.path
import re


if __name__ == '__main__':
    arg = sys.argv

    if len(arg) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = arg[1]
    output_file_name = arg[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Markdown headings to HTML tags
    with open("README.md", mode="r") as f:
        content = f.read()

    # I used regex to look for the '#'
    markdown_headings = re.compile(r"^(#{1,6})\s+(.*)$", flags=re.MULTILINE)

    # I used re.sub with a lambda function to
    # replace all Markdown headings with  HTML headings
    html_content = markdown_headings.sub(
        lambda match: f"<h{len(match.group(1))}>\
        {match.group(2)}</h{len(match.group(1))}>",
        content,
    )
    # Write the HTML content to the output file
    with open(output_file_name, mode="w") as f:
        f.write(html_content)

    sys.exit(0)
