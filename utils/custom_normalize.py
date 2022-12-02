import re


class CusNormalizer():
    def __init__(self):
        self.regex = re.compile(r'\n(\s)*\n')

    def normalize(self, text):
        text1 = text
        while True:
            final_text = text1
            all_matches = list(re.finditer(self.regex, text1))
            if not all_matches:
                break
            for matched in all_matches:
                start, end = matched.span()
                final_text = text1[:start - 1] + '\n' + text1[end:]
            text1 = final_text
        return final_text
