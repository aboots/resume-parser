import re


class EmploymentStatusExtractor:
    def __init__(self) -> None:
        pass

    def find(self, text, job_text):
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
        pattern_keys = r"({})\s*:*".format("|".join(keys))
        pattern_values = r"({})".format("|".join(values))
        pattern_up_to_now = r"({})".format("|".join(up_to_now))
        text = re.sub(r"\n+", r" ", text)
        text = re.sub(r"\s+", r" ", text)
        for match_key in re.finditer(pattern_keys, text):
            for match_value in re.finditer(
                pattern_values, text[match_key.end() : match_key.end() + 40]
            ):
                return match_value.group(1)
        if len(re.findall(pattern_up_to_now, job_text)) != 0:
            return "تا کنون شاغل"
        return None
