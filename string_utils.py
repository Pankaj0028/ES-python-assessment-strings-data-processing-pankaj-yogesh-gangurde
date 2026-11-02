"""Python Programming Assessment: Strings & Data Processing."""


def reverse_string(text: str) -> str:
    """Return the reverse of the given string."""
    reversed_text = ""
    for char in text:
        # Put each new character in front of the result built so far
        reversed_text = char + reversed_text
    return reversed_text


def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u) in the string, ignoring case."""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(reverse_string("hello"))       # olleh
    print(count_vowels("Hello World"))   # 3
