import pandas as pd


class JobTitleFinder:
    def __init__(self) -> None:
        titles = list(
            pd.read_csv(
                "cv_info_extractor/resources/jobs.csv",
            )["title"]
        )
        expanded_1 = [
            text.replace("مهندس", "مهندسی") for text in titles if "مهندس" in text
        ]
        titles += expanded_1
        self.titles = sorted(titles, key=lambda s: -len(s))
        self.normalized_title = [self.normalize(text) for text in self.titles]

    def normalize(self, txt):
        txt = txt.replace(" ", "")
        txt = txt.replace("\n", "")
        txt = txt.replace("\u200C", "")
        return txt

    def find(self, text):
        normalized_text = self.normalize(text)
        min_index = float("inf")
        for idx, title in enumerate(self.normalized_title):
            if title in normalized_text:
                index = normalized_text.index(title)
                if index < min_index:
                    return self.titles[idx]
        return 'None'