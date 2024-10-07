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

## Requirements

- Python 3.x
- `hazm` library for Persian text processing

## Usage

1. Prepare your input file (`input_text.md`) with the Persian text you want to normalize.
2. Run the program to normalize the text.
3. See the output text on (`output_text.md`)
