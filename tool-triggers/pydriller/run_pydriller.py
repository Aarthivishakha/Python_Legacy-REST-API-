import sys

from pydriller import Repository


def main():
    repository = sys.argv[1] if len(sys.argv) > 1 else "."
    for commit in Repository(repository, filepath="legacy_api").traverse_commits():
        print("%s %s" % (commit.hash[:12], commit.msg.splitlines()[0]))


if __name__ == "__main__":
    main()
