# Text only scanner
This plugin reads and scans all the files in a particular folder and will flag out files that contains outside alpha-numeric keyboard charaters or binary files. 

## Objective
The objective of this library is to ensure only text based files that are readable to the human eyes get pass through the tests and fails everything else.

## Usage

You can use the library from Python::

```py
from text_only_scanner.detector import is_text_file, filter_text_files

print(is_text_file("somefile.txt"))

accepted, rejected = filter_text_files(["a.txt", "b.bin"])
print("accepted:", accepted)
print("rejected:", rejected)
```

Or use the CLI entrypoint::

```bash
python -m text_only_scanner.cli file1.txt file2.bin
# prints accepted files to stdout, rejected to stderr and exits non-zero if any rejected
```

Notes:
- The detector uses a conservative heuristic (NUL bytes and control-character ratio) to
	decide whether a file is text. It is designed to match common editor behavior and is
	fast and dependency-free.

Recursive usage:

```bash
# Recurse into directories and check all files inside
python -m text_only_scanner.cli -r pass_folder fail_folder
```
