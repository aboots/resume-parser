import re
import hazm


class SectionExtractor:
    def __init__(self):
        with open('cv_info_extractor/resources/keywords.txt', 'r', encoding="utf-8") as file:
            self.keywords = [l.strip() for l in file.readlines()]

    def match_sections(self, inp):
        idxs = [inp.find(k) for k in self.keywords if inp.find(k) != -1]
        idxs.append(len(inp))
        idxs.sort()
        print(idxs)
        matches = [inp[idxs[i]:idxs[i + 1]] for i in range(len(idxs) - 1)]
        return matches

    def find_sections(self, text):
        matched_sections = self.match_sections(text)
        if not matched_sections:
            return 'Not Found'
        return matched_sections
