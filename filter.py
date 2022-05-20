from panflute import *
import sys

headers = []

def change_header_level(elem, _):
    if isinstance(elem, Header) and elem.level > 2:
        return Header(Str(stringify(elem).upper()), level=elem.level)

def change_bold_word(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))

def header_repeat_warning(elem):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write("Warning! Header repeated: " + stringify(elem))
        else:
            headers.append(stringify(elem))

if __name__ == "__main__":
    run_filters([header_repeat_warning, change_header_level], prepare=change_bold_word)
