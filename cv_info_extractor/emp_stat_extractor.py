import re


class EmploymentStatusExtractor:
    def __init__(self) -> None:
        keys = [
            "وﺿﻌﯿﺖ اﺷﺘﻐﺎل",
            "وضعیت اشتغالی",
            "وضعیت استخدام",
            "وضعیت استخدامی",
            "وضعیت کار",
            "وضعیت کاری",
        ]
        values = [
            "علاقه مند",
            "علاقه‌مند",
            "ﻋﻼﻗﻪ ﻣﻨﺪ",
            "بیکار",
            "مشغول",
            "شاغل",
        ]
        up_to_now = [
            "تاکنون",
            "تا اکنون",
            "تا زمان حال",
            "تا حال",
            "تا الان",
            "تا الآن",
        ]
        self.pattern_keys = r"({})\s*:*".format("|".join(keys))
        self.pattern_values = r"({})".format("|".join(values))
        self.pattern_up_to_now = r"({})".format("|".join(up_to_now))

    def find(self, text1, job_text):
        text = text1
        text = re.sub(r"\n+", r" ", text)
        text = re.sub(r"\s+", r" ", text)
        for match_key in re.finditer(self.pattern_keys, text):
            for match_value in re.finditer(
                self.pattern_values, text[match_key.end() : match_key.end() + 40]
            ):
                return match_value.group(1)
        if len(re.findall(self.pattern_up_to_now, job_text)) != 0:
            return "تا کنون شاغل"
        return "None"
