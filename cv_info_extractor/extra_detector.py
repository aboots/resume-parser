import re
import hazm


class ExtraDetection:
    def __init__(self):
        with open('cv_info_extractor/resources/last_names_regex.json', 'r', encoding="utf-8") as file:
            self.keywords = file.readlines()

    def match_email(self, inp):
        idxs = [inp.find(k) for k in self.keywords]    
        matches = []
        for keyword_count in range(10, 0, -1):
            count_pattern = self.pattern.format()
            for matched in re.finditer(count_pattern, inp):
                start, end = matched.span()
                inp = inp[:start] + '#' * (end - start) + inp[end:]
                matches.append(matched)
        return matches

    def find_extra(self, text):
        
        matched_emails = self.match_email(text)
        if not matched_emails:
            return 'Not Found'
        return matched_emails[0].group().strip()