import re

import hazm

INPUT_FILE = "input_text.md"
OUTPUT_FILE = "output_text.md"

class TextNormalizer:

    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path or INPUT_FILE
        self.output_path = output_path or OUTPUT_FILE
        self.normalizer = hazm.Normalizer(
            persian_style=False,
            unicodes_replacement=False,
            persian_numbers=False,
            remove_diacritics=False,
            remove_specials_chars=False,
            decrease_repeated_chars=False,
        )

    def read_text_from_file(self):
        try:
            with open(self.input_path, 'r', encoding='utf-8') as file:
                return file.read()
        except (FileNotFoundError, Exception) as e:
            print(f"Error reading file: {e}")
            return ""

    def write_text_to_file(self, text):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Normalized text written to {self.output_path}")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def normalize_text(self):
        text = self.read_text_from_file()
        if not text:
            return

        skip_patterns = re.compile(
            r'('
            r'</?[a-zA-Z][^>]*>|'  # All HTML-like tags, including closing tags
            r'[*]+[^*]+[*]+|'  # Bold and italic (Markdown)
            r'/[^/]+/|'  # Slashes
            r'`[^`]+`|'  # Inline code
            r'[{}[\]]|'  # Brackets
            r'%|'  # Percentage
            r'^\s*!.*$'  # Lines starting with !
            r')',
            re.MULTILINE
        )
        parts = skip_patterns.split(text)
        normalized_parts = [
            self.normalizer.normalize(part) if not skip_patterns.match(part) else part
            for part in parts
        ]
        normalized_text = ''.join(normalized_parts)

        punctuation_replacements = {
            '* (': '*(',
            ') *': ')*',
            '* [': '*[',
            '] *': ']*',
            '* ،': '*،',
            '* .': '*.',
            '! ': '!',
            ' !': '!',
        }

        for old, new in punctuation_replacements.items():
            normalized_text = normalized_text.replace(old, new)

        self.write_text_to_file(normalized_text)


text_normalizer = TextNormalizer()
text_normalizer.normalize_text()
