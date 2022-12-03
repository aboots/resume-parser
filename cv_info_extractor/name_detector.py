import json
import re


class NameDetection:
    def __init__(self):
        with open('cv_info_extractor/resources/last_names_regex.json', 'r', encoding="utf-8") as file:
            self.last_names_reg = json.loads(file.read())

        with open('cv_info_extractor/resources/first_names_regex.json', 'r', encoding="utf-8") as file:
            self.first_names_reg = json.loads(file.read())

        self.pattern = f"(^|\W)((((({self.first_names_reg})(\W+))+)({self.last_names_reg}))|(((({self.first_names_reg})(\W+))+)(\w+))|({self.last_names_reg})|({self.first_names_reg}))($|\W)"
        # self.pattern = f"(^|\W)((((({self.first_names_reg})(\W+))+)({self.last_names_reg}))|({self.last_names_reg})|({self.first_names_reg}))($|\W)"
        # self.pattern2 = f"(^|\W)(((({self.first_names_reg})(\W+))+)(\w))($|\W)"
        # self.pattern2 = f"(((({self.first_names_reg})(\W+))+)(\w))"
        # self.pattern = f"(^|\W)((((({self.first_names_reg})(\W+))+)({self.last_names_reg}))|({self.last_names_reg})|({self.first_names_reg}))($|\W)"

    def match_name(self, inp):
        matches = []
        count_pattern = self.pattern.format()
        for matched in re.finditer(count_pattern, inp):
            start, end = matched.span()
            inp = inp[:start] + '#' * (end - start) + inp[end:]
            matches.append(matched)
        return matches

    def find_name(self, text):
        matched_names = self.match_name(text)
        if not matched_names:
            return ['Not Found'] * 3
        full_name = matched_names[0].group().strip()
        if matched_names[0].groups()[3]:
            first_name = matched_names[0].groups()[3].strip()
        elif len(matched_names[0].groups()) > 9 and matched_names[0].groups()[9]:
            first_name = matched_names[0].groups()[9].strip()
        else:
            first_name = 'None'
        if len(matched_names[0].groups()) > 7 and matched_names[0].groups()[7]:
            last_name = matched_names[0].groups()[7].strip()
        elif matched_names[0].groups()[-4]:
            last_name = matched_names[0].groups()[-4].strip()
        else:
            last_name = 'None'
        return full_name, first_name, last_name
