import os, sys

# Ensure project root is on sys.path so local package can be imported
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root)

from text_only_scanner.detector import filter_text_files
folders = [os.path.join(root, "pass_folder"), os.path.join(root, "fail_folder")]
files = []
for folder in folders:
    if os.path.isdir(folder):
        for dirpath, _, filenames in os.walk(folder):
            for fn in filenames:
                files.append(os.path.join(dirpath, fn))
    else:
        print(f"Folder not found: {folder}", file=sys.stderr)

accepted, rejected = filter_text_files(files)
print("ACCEPTED:")
for a in accepted:
    print(a)

print("REJECTED:", file=sys.stderr)
for r in rejected:
    print(r, file=sys.stderr)

print(f"SUMMARY: accepted={len(accepted)} rejected={len(rejected)}")
