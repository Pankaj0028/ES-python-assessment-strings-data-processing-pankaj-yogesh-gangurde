# Python Programming Assessment: Strings & Data Processing

My name is Pankaj Yogesh Gangurde. I am applying for the Python Developer Intern role at Embed Square Solutions Pvt. Ltd.

- **Full Name:** Pankaj Yogesh Gangurde
- **GitHub:** https://github.com/Pankaj0028/ES-python-assessment-strings-data-processing-pankaj-yogesh-gangurde
- **Submission Date:** 02 November 2026

## What I built

This small project has two functions.

`reverse_string` takes a word or sentence and gives it back backwards. For example, `hello` becomes `olleh`.

`count_vowels` counts how many vowels are in the text. The vowels are a, e, i, o, and u. Capital letters count too, so `Hello World` has 3 vowels.

## How I did it

**Reversing a string**

I start with an empty result. I look at each letter from left to right. Each new letter is placed at the front of the result, so the first letter ends up at the end. If the text is empty, the function just returns an empty string.

**Counting vowels**

I first turn the whole text into lowercase, so `A` and `a` are treated the same. Then I check every character. If it is one of `a`, `e`, `i`, `o`, or `u`, I add 1 to a counter. At the end I return that number. Spaces, numbers, and symbols are ignored.

## What I checked

- An empty string
- Capital and small letters
- Text with spaces
- Words that have no vowels, such as `rhythm`

I also tried the functions on 60 sample strings: short words, sentences, and a few odd cases.

## Files

| File | What it does |
|------|----------------|
| `string_utils.py` | The two functions |
| `sample_strings.py` | The 60 sample strings |
| `run_samples.py` | Prints a table for every sample |
| `test_string_utils.py` | Checks that the functions work |

## How to run

From this folder, run:

```bash
python string_utils.py
python run_samples.py
python -m unittest -v
```

The first command prints two examples: `olleh` and `3`.  
The second command prints all 60 strings with the reversed text and the vowel count.  
The third command runs the tests.
