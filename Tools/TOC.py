# Just a helper file to auto generate table of contents for myslef in my MD files
import re

def generateTOC(path: str)->None:

    heading_regex = r'^(#+)\s*(.+?)(\s*\(.*?\))?$'

    headings = []


    with open(path,"r") as file:

        lines = file.read()
        print(lines)
        for line in lines:
            if re.match(heading_regex, line):
                print(line)


if __name__ == "__main__":

    markdown_path = input("Please enter the path of the MD file you wish to generate a table of contents for: ")

    generateTOC(markdown_path)