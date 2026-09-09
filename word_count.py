import sys


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()

    print(count_words(text))


if __name__ == "__main__":
    main()
