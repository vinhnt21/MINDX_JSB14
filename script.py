import os
import argparse
import sys

#!/usr/bin/env python3
# script.py - In ra toàn bộ file/folder con bên trong folder "final-project" (mặc định)

def list_tree(path, prefix=""):
    try:
        entries = sorted(os.listdir(path))
    except FileNotFoundError:
        print(f'Error: path not found: {path}', file=sys.stderr)
        return
    except PermissionError:
        print(f'Error: permission denied: {path}', file=sys.stderr)
        return

    for i, name in enumerate(entries):
        full = os.path.join(path, name)
        is_dir = os.path.isdir(full)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + (name + "/" if is_dir else name))
        if is_dir:
            extension = "    " if i == len(entries) - 1 else "│   "
            list_tree(full, prefix + extension)

def main():
    p = argparse.ArgumentParser(description="In ra toàn bộ file/folder con bên trong folder (mặc định: ./final-project)")
    p.add_argument("path", nargs="?", default="final-project", help="đường dẫn tới folder (mặc định: final-project)")
    args = p.parse_args()
    root = args.path
    if not os.path.exists(root):
        print(f'Error: path not found: {root}', file=sys.stderr)
        sys.exit(1)
    print(os.path.basename(os.path.abspath(root)) + "/")
    list_tree(root)

if __name__ == "__main__":
    main()