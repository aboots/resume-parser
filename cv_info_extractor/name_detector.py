import json
import re


class NameDetection:
    def __init__(self):
        file = open('cv_info_extractor/resources/last_names_regex.json', 'r', encoding="utf-8")
        self.last_names_reg = json.loads(file.read())
        file.close()

        file = open('cv_info_extractor/resources/first_names_regex.json', 'r', encoding="utf-8")
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

    def find_name(self, text):
        matched_names = self.match_name(text)
        if not matched_names:
            return 'Not Found'
        return matched_names[0].group().strip()
