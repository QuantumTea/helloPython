import os

# https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python/52132574
script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
rel_path = "wordcount.csv"
abs_file_path = os.path.join(script_dir, rel_path)


def does_file_exist():
    f = open(abs_file_path)
    contents = f.read()
    f.close()
    return contents
