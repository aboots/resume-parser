import re


class JobExpectedExtractor:
    def __init__(self) -> None:
        keys = [
            "نوع شغل موردنظر",
            "شغل موردنظر",
            "شغل دلخواه",
            "ﻧﻮع ﺷﻐﻞ ﻣﻮرد ﻧﻈﺮ",
        ]
        values = [
            "ﺗﻤﺎم وﻗﺖ",
            "تمام وقت",
            "پاره وقت",
            "کارآموزی",
        ]
        self.pattern_keys = r"({})\s*:*".format("|".join(keys))
        self.pattern_values = r"({})".format("|".join(values))

    def find(self, text1):
        text = text1
        text = re.sub(r"\n+", r" ", text)
        text = re.sub(r"\s+", r" ", text)
        for match_key in re.finditer(self.pattern_keys, text):
            for match_value in re.finditer(
                self.pattern_values, text[match_key.end() : match_key.end() + 40]
            ):
                return match_value.group(1)
        return "None"
