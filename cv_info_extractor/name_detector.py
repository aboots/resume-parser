import json
import re


class NameDetection:
    def __init__(self):
        file = open('resources/last_names_regex.json', 'r', encoding="utf-8")
        self.last_names_reg = json.loads(file.read())
        file.close()

        file = open('resources/first_names_regex.json', 'r', encoding="utf-8")
        self.first_names_reg = json.loads(file.read())
        file.close()

        self.pattern = f"(^|\W)(((({self.first_names_reg})(\W+))+({self.last_names_reg}))|({self.last_names_reg})|({self.first_names_reg}))($|\W)"

    def match_name(self, inp):
        matches = []
        for keyword_count in range(10, 0, -1):
            count_pattern = self.pattern.format()
            for matched in re.finditer(count_pattern, inp):
                start, end = matched.span()
                inp = inp[:start] + '#' * (end - start) + inp[end:]
                matches.append(matched)
        return matches

    def hide_person_name(self, text):
        matched_names = self.match_name(text)
        for i in matched_names:
            text = text.replace(i.group(), " <#person_name#> ")
        return text.strip()
