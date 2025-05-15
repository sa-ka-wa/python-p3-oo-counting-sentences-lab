#!/usr/bin/env python3
# lib/count_sentences.py

class MyString:
    def __init__(self, string=""):
        self.value = string

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, string):
        if not isinstance(string, str):
            print("The value must be a string.")
            return
        self._value = string
  

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # Split by '.', '!', '?' followed by space or end of string
        sentences = re.split(r'[.!?]', self.value)
        return len([s for s in sentences if s.strip()])
