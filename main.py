import sys
from stats import count_words,count_char,show_report

def get_book_test(filepath:str):
    with open(filepath) as f:
        contents=f.read()
    return contents

def main():
    if len(sys.argv)!=2:
        print("NOT ENOUGH ARGUMENTS\nUsage: python3 main.py <path_to_book>")
        sys.exit(1)
    rel_path=sys.argv[1]
    contents=get_book_test(rel_path)
    show_report(count_char(contents),count_words(contents))
    
main()