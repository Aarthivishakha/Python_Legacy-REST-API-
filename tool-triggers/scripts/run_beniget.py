import ast
import pathlib
import sys

import beniget


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "legacy_api")
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        beniget.DefUseChains().visit(tree)
        print(path)


if __name__ == "__main__":
    main()
