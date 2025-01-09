#!/usr/bin/python3
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_markdown_file> <output_html_file>", file=sys.stderr)
        sys.exit(1)

    input_markdown_file = sys.argv[1]

    if not os.path.exists(input_markdown_file):
        print(f"Missing {input_markdown_file}", file=sys.stderr)
        sys.exit(1)

    # If both checks pass, exit with status 0
    sys.exit(0)

if __name__ == "__main__":
    main()
