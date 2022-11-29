import re
from persiantools import digits


class DateDetection:
    def __init__(self):
        self.pattern1 = r'\d{1,2}(\s*)?(?:فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)(\s*)?\d{2,4}'
        self.pattern1 = r'\d{2,4}(\s*)?(?:فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)(\s*)?\d{1,2}'
        self.pattern2 =r'\d{2,4}/\d{1,2}/\d{1,2}'
        self.pattern = f'{self.pattern1}|{self.pattern2}'

    def match_date(self, inp1):
        matches = []
        inp = digits.fa_to_en(inp1)
        print(inp)
        for matched in re.finditer(self.pattern, inp):
            start, end = matched.span()
            inp = inp[:start] + '#' * (end - start) + inp[end:]
            matches.append(matched)
        return matches

    def find_date_number(self, text):
        matched_dates = self.match_date(text)
        if not matched_dates:
            matched_dates = self.match_date(text[::-1])
            if not matched_dates:
                return 'Not Found'
            return matched_dates[0].group().strip()
        return matched_dates[0].group().strip()
