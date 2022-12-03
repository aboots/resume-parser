import re
from persiantools import digits


class PhoneNumberDetection:
    def __init__(self):
        self.pattern1 = r"(^|\W)((\+98|0)?9\d{9})($|\W)"
        self.pattern2 = r"(^|\W)((\+98|0)(\s)?9\d{9})($|\W)"
        self.pattern3 = r"(^|\W)((\+98|0)(\s)?(9\d{2})(\s)?(\d{4})(\s)?(\d{3}))($|\W)"
        self.pattern4 = r"(^|\W)(\(\+98\)?9\d{9})($|\W)"
        self.pattern5 = r"(^|\W)((\+98|0)(\s)*(9\d{2})(\s)*(\d{3})(\s)*(\d{4}))($|\W)"
        self.pattern = f'{self.pattern1}|{self.pattern2}|{self.pattern3}|{self.pattern4}|{self.pattern5}'

    def match_phone_number(self, inp1):
        matches = []
        inp = digits.fa_to_en(inp1)
        for matched in re.finditer(self.pattern, inp):
            start, end = matched.span()
            inp = inp[:start] + '#' * (end - start) + inp[end:]
            matches.append(matched)
        return matches

    def find_phone_number(self, text):
        matched_phones = self.match_phone_number(text)
        if not matched_phones:
            matched_phones = self.match_phone_number(text[::-1])
            if not matched_phones:
                return 'Not Found'
            return matched_phones[0].group().strip()
        return matched_phones[0].group().strip()