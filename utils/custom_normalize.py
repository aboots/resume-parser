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


class PersianNormalizer():
    def __init__(self):
        with open('cv_info_extractor/resources/normalizer_correct.txt', 'r', encoding="utf-8") as file:
            self.keywords = [l.strip().split(',') for l in file.readlines()]
        self.dic = {i[1]: i[0] for i in self.keywords}

    def normalize(self, text):
        text2 = ''
        for i in text:
            if i in self.dic:
                text2 += self.dic[i]
            else:
                text2 += i
        return text2