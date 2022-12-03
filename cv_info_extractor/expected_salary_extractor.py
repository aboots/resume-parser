import re


class ExpectedSalaryExtractor:
    def __init__(self) -> None:
        keys = [
            "حقوق موردانتظار",
            "ﺣﻘﻮق ﻣﻮرداﻧﺘﻈﺎر",
            "ﺣﻘﻮق مدنظر",
            "حقوق دلخواه",
        ]
        self.pattern_keys = r"({})\s*:*".format("|".join(keys))

    def find(self, text1):
        text = text1
        for match_key in re.finditer(self.pattern_keys, text):
            text2 = text[match_key.end():]
            if text2.find('\n') != -1:
                return text2[:text2.find('\n')]
            return text2
        return "None"
