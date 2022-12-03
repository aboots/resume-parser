import pandas as pd
import re


class CityProvinceExtractor:
    def __init__(self):
        df = pd.read_csv("cv_info_extractor/resources/cities.csv")
        self.cities = set(df["city"].to_list())
        self.provinces = set(df["province"].to_list())
        self.common_names = set.intersection(self.cities, self.provinces)

    def find(self, original_text):
        original_text = re.sub(r"[^\w\s]", "", original_text)
        original_text = re.sub(r"\s+", " ", original_text)
        original_text = re.sub(r"\n", " ", original_text)
        text = original_text

        for common_name in self.common_names:
            text = text.replace(common_name, "#" * len(common_name))
        for city in self.cities:
            text = text.replace(city, "&" * len(city))
        for province in self.provinces:
            text = text.replace(province, "*" * len(province))

        matches = []

        for match in re.finditer(r" ([#|&]+) ([#|*]+) ", text):
            city = original_text[match.span(1)[0]: match.span(1)[1]]
            province = original_text[match.span(2)[0]: match.span(2)[1]]
            text = (
                    text[: match.start()]
                    + "~" * (match.end() - match.start())
                    + text[match.end():]
            )
            matches.append({"city": city, "province": province})
        for match in re.finditer(r" ([#|&]+) استان ([#|*]+) ", text):
            city = original_text[match.span(1)[0]: match.span(1)[1]]
            province = original_text[match.span(2)[0]: match.span(2)[1]]
            text = (
                    text[: match.start()]
                    + "~" * (match.end() - match.start())
                    + text[match.end():]
            )
            matches.append({"city": city, "province": province})
        for match in re.finditer(r" ([#|*]+) ", text):
            province = original_text[match.span(1)[0]: match.span(1)[1]]
            text = (
                    text[: match.start()]
                    + "~" * (match.end() - match.start())
                    + text[match.end():]
            )
            matches.append({"city": None, "province": province})
        if not matches:
            return [{"city": 'None', "province": 'None'}]
        return matches
