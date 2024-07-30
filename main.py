#!/usr/bin/env python

import argparse
import mistune
import sys


def extract_header(md_content):
    # extract header section between `--- head` and `---`
    header = {}
    in_header = False
    header_lines = []
    stylesheets = []

    for line in md_content.splitlines():
        if line.strip() == "--- head":
            in_header = True
            continue
        elif line.strip() == "---" and in_header:
            in_header = False
            break

        if in_header:
            header_lines.append(line)

    for line in header_lines:
        if line.lower().startswith("title:"):
            header["title"] = line[len("title:") :].strip().strip('"')
        elif line.lower().startswith("stylesheet:") or line.lower().startswith(
            "style:"
        ):
            stylesheet = line.split(":", 1)[1].strip().strip('"')
            stylesheets.append(stylesheet)

    if stylesheets:
        header["stylesheets"] = stylesheets

    return header


def convert_md_to_html(input_file, output_file):
    # read the markdown file
    with open(input_file, "r", encoding="utf-8") as file:
        md_content = file.read()

    # extract header
    header = extract_header(md_content)

    # remove the header section from markdown content
    if "--- head" in md_content and "---" in md_content:
        md_content = md_content.split("---", 2)[-1].strip()

    # convert markdown to html using mistune
    markdown = mistune.create_markdown(renderer=mistune.HTMLRenderer(escape=False))
    html_content = markdown(md_content)

    # create full html content with header and stylesheet
    stylesheet_links = "\n".join(
        f'<link rel="stylesheet" href="{stylesheet}">'
        for stylesheet in header.get("stylesheets", [])
    )

    full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{header.get('title', 'Untitled')}</title>
    {stylesheet_links}
</head>
<body>
    {html_content}
</body>
</html>
    """

    # write the full html content to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(full_html)


def main():
    # setup command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to an HTML file with optional headers and stylesheets."
    )
    parser.add_argument("input", help="Path to the input Markdown file")
    parser.add_argument("output", help="Path to the output HTML file")

    # check if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # parse arguments
    args = parser.parse_args()

    # convert markdown to html
    convert_md_to_html(args.input, args.output)


if __name__ == "__main__":
    main()
