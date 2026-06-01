# Just a helper file to auto generate table of contents for myslef in my MD files
import re
import string
from typing import List

def format_heading(heading:str)-> str:

    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + ' '
    heading = ''.join(e for e in heading if e in allowed_chars) # May not be correct for heading formats in general but its a tool for me
    heading = re.sub(r'\s+', '-', heading)
    heading = heading.lower() 

    return f"#{heading}"

def grab_headings(lines: List[str]) -> List[str]:

    heading_regex = r'^(#+)\s*(.+?)(\s*\(.*?\))?$'
    headings = {}
    for line in lines:
        if re.match(heading_regex, line):
            title = line.replace('#','')
            title = title.replace('\n','')
            title = title[1:]
            headings[title] = f"{format_heading(title)}"

    return headings

def generate_TOC(path: str)->None:

    #general format to follow

    # Table of contents
    # 1. [Literal name of heading](#literal-name-of-heading)
    # 2. [Some other heading](#some-other-heading)

    counter = 1
    table_of_contents = ["# Table of contents\n\n"]

    try:

        with open(path,mode="r",encoding="utf-8") as file:

            contents = file.readlines()
            headings = grab_headings(contents)

            for k in headings:
                table_of_contents.append(f"{counter}. [{k}]({headings[k]})\n")
                counter += 1

            contents = table_of_contents + contents + ["\n"]

        with open(path,mode="w",encoding="utf-8") as file:
            file.writelines(contents)

    except FileNotFoundError as FE:
        print(f"Error detected, possible not file found error. Ensure that the path is correct. The path needs to be either absolute or relative from the current execution location.\n\nERROR: {FE}")
        exit(1)

if __name__ == "__main__":

    markdown_path = input("Please enter the path of the MD file you wish to generate a table of contents for: ")

    headings = generate_TOC(markdown_path)