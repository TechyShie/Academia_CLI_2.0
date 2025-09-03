import os
import sys
from io import StringIO
import tokenize as tz

EXCLUDE_DIRS = {
    '__pycache__', '.git', '.hg', '.svn', '.mypy_cache', '.pytest_cache',
    'venv', '.venv', 'env', 'build', 'dist', '.idea', '.vscode'
}

def remove_comments_and_docstrings(source: str) -> str:

    io_obj = StringIO(source)
    out = []

    prev_toktype = tz.INDENT
    last_lineno = -1
    last_col = 0

    try:
        tokgen = tz.generate_tokens(io_obj.readline)
    except Exception:
        tokgen = tz.tokenize(io_obj.readline)

    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:

        if toktype == tz.COMMENT:
            continue

        if toktype == tz.STRING:
            if prev_toktype in {tz.INDENT, tz.NEWLINE} or last_lineno == 0:

                if ltext is None or ltext.strip().startswith(ttext):

                    continue

        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            out.append(" " * (scol - last_col))

        out.append(ttext)

        prev_toktype = toktype
        last_lineno = elineno
        last_col = ecol

    return "".join(out)

def source_endswith_newline(s: str) -> bool:
    return s.endswith("\n") or s.endswith("\r\n")

def clean_blank_lines(s: str) -> str:

    lines = s.splitlines()
    new_lines = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count > 1:
                continue
        else:
            blank_count = 0
        new_lines.append(line.rstrip())
    return "\n".join(new_lines) + ("\n" if source_endswith_newline(s) else "")

def process_file(path: str) -> bool:

    try:
        with open(path, 'r', encoding='utf-8', errors='surrogatepass') as f:
            src = f.read()
    except Exception:
        with open(path, 'r', encoding='latin-1') as f:
            src = f.read()

    stripped = remove_comments_and_docstrings(src)
    stripped = clean_blank_lines(stripped)

    if stripped != src:
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(stripped)
        return True
    return False

essages = []

def main() -> int:
    changed = 0
    files = 0

    for root, dirs, filenames in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name.endswith('.py'):
                path = os.path.join(root, name)
                files += 1
                try:
                    if process_file(path):
                        changed += 1
                        print(f"Stripped comments: {path}")
                except Exception as e:
                    print(f"Failed to process {path}: {e}")

    print(f"Processed {files} .py files, changed {changed}.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
