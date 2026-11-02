"""Run both functions on all sample strings and print a results table."""

from string_utils import reverse_string, count_vowels
from sample_strings import SAMPLE_STRINGS


def main() -> None:
    print(f"{'No.':<4} {'Original':<48} {'Reversed':<48} Vowels")
    print("-" * 110)
    for number, text in enumerate(SAMPLE_STRINGS, start=1):
        print(f"{number:<4} {repr(text):<48} {repr(reverse_string(text)):<48} {count_vowels(text)}")
    print("-" * 110)
    print(f"Total strings processed: {len(SAMPLE_STRINGS)}")


if __name__ == "__main__":
    main()
