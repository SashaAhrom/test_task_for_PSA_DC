import os
import re
import sys


def convert_case(match_obj):
    """Concatenates groups."""
    return match_obj.group(1) + match_obj.group(3)


def parameter_replacement(directory_path):
    """Equates a variable to a variable from the cast method."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                path_file = os.path.join(root, file)
                with open(path_file, 'r') as f1:
                    date = f1.read()
                    new_date = re.sub(r'([\S]+  ?= ?)cast\(\w+(\[.*])?, ?(.+)\)', convert_case, date)
                with open(path_file, 'w') as f1:
                    f1.write(new_date)


if __name__ == "__main__":
    for address in sys.argv[1:]:
        parameter_replacement(address)
