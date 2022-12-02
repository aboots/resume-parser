import json
import re


class EmailDetection:
    def __init__(self):
        self.pattern = r"\b(\w+([-+(\.|\[dot\])']\w+)*(@|\[at\])\w+([-(\.|\[dot\])]\w+)*(\.|\[dot\])\w+([-(\.|\[dot\])]\w+)*)\b"

    def match_email(self, inp):
        matches = []
        count_pattern = self.pattern.format()
        for matched in re.finditer(count_pattern, inp):
            start, end = matched.span()
            inp = inp[:start] + '#' * (end - start) + inp[end:]
            matches.append(matched)
        return matches

    def find_email(self, text):
        matched_emails = self.match_email(text)
        if not matched_emails:
            return 'Not Found'
        return matched_emails[0].group().strip()
