#!/usr/bin/python3

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

    with open(markdown_file, mode="r") as f:
        content = f.read()

    # MARKDOWN TO HTML HEADINGS
    markdown_headings = re.compile(r"^(#{1,6})\s+(.*)$", flags=re.MULTILINE)
    html_headings = markdown_headings.sub(
        lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>",
        content
    )

    # MARKDOWN TO HTML UNORDERED LISTS
    unordered_listing = re.compile(r"^\s*-\s+(.*)$", flags=re.MULTILINE)
    matches = unordered_listing.findall(content)
    html_unordered_lists = ""
    if matches:
        html_unordered_lists = "<ul>\n"
        for match in matches:
            html_unordered_lists += f"    <li>{match}</li>\n"
        html_unordered_lists += "</ul>"

    # Combine HTML content from both processes
    html_content = html_headings + '\n' + html_unordered_lists

    # Write the HTML content to the output file
    with open(output_file_name, mode="w") as f:
        f.write(html_content)

    sys.exit(0)
