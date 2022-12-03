import re
from persiantools import digits


class DateDetection:
    def __init__(self):
        self.pattern1 = r'\d{1,2}(\s*)?(?:فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)(\s*)?\d{2,4}'
        self.pattern2 = r'\d{2,4}(\s*)?(?:فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)(\s*)?\d{1,2}'
        self.pattern3 = r'\d{2,4}/\d{1,2}/\d{1,2}'
        self.pattern = f'{self.pattern1}|{self.pattern2}|{self.pattern3}'
        self.keywords = [
            'متولد',
            'تولد',
            'ولادت',
        ]

    def match_date(self, inp1):
        matches = []
        inp = digits.fa_to_en(inp1)
        for matched in re.finditer(self.pattern, inp):
            start, end = matched.span()
            inp = inp[:start] + '#' * (end - start) + inp[end:]
            matches.append(matched.group().strip())
        return matches

    def find_date_number(self, text):
        for keyword in self.keywords:
            if keyword not in text:
                continue
            text1 = text[text.find(keyword):]
            matched_dates = self.match_date(text1)
            if not matched_dates:
                matched_dates = self.match_date(text1[::-1])
                if not matched_dates:
                    return 'Not Found'
                return matched_dates[0]
            return matched_dates[0]
        return 'Not Found'
