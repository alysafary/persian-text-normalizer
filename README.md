# Persian Text Normalizer

A Python project that normalizes Persian text while preserving specific formatting such as punctuation marks, special
tags (like HTML or Markdown), bold, italics, and slashes. It is based on the `hazm` library and is designed to process
input text files, apply custom text normalization, and write the normalized text to an output file.

## Features

- Normalizes Persian text (e.g., fixing spaces, reducing repeated characters).
- Preserves special formatting like:
    - HTML/XML tags (e.g., `<mark>`, `<b>`, etc.).
    - Markdown-like syntax (e.g., `**bold**`, `*italic*`).
    - Special characters and slashes (e.g., `/example/`).
- Custom punctuation handling (e.g., proper spacing around punctuation like commas and parentheses).

## Important Note

When using asterisks (*) or underscores (_) for emphasis or special formatting (e.g., *bold*, _italic_), do not place
them immediately before punctuation marks like colons, commas, or periods. For example, the following is incorrect:

- Incorrect: `_word:_` or `**word:**` or `*word:*`

In these cases, the punctuation should come after the closing asterisk or underscore, with no punctuation immediately
following the special formatting. The correct versions are:

- Correct: `_word_:` or `**word**:` or `*word*:`

## Requirements

- Python 3.x
- `hazm` library for Persian text processing

## Usage

1. Prepare your input file (`input_text.md`) with the Persian text you want to normalize.
2. Run the program to normalize the text.
3. See the output text on (`output_text.md`)
