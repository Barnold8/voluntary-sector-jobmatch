# Just a helper file to auto generate table of contents for myslef in my MD files
import re
import string
from typing import List

# List[str]

def format_heading(heading:str)-> str:

    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + '#' + ' '
    heading = ''.join(e for e in heading if e in allowed_chars) # May not be correct for heading formats in general but its a tool for me
    heading = re.sub(r'\s+', '-', heading)

    return heading

def grab_headings(lines: List[str]) -> List[str]:

    heading_regex = r'^(#+)\s*(.+?)(\s*\(.*?\))?$'
    headings = []
    for line in lines:
        if re.match(heading_regex, line):
            heading = format_heading(line)
            headings.append(heading)
    return headings


def generate_TOC(path: str)->None:

    try:

        with open(path,mode="r",encoding="utf-8") as file:
            headings = grab_headings(file.readlines())

            for heading in headings:
                # print(heading)
                pass


    except FileNotFoundError as FE:
        print(f"Error detected, possible not file found error. Ensure that the path is correct. The path needs to be either absolute or relative from the current execution location.\n\nERROR: {FE}")
        exit(1)


if __name__ == "__main__":

    markdown_path = input("Please enter the path of the MD file you wish to generate a table of contents for: ")

    headings = generate_TOC(markdown_path)