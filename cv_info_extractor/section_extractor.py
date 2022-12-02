import re
import hazm


class SectionExtractor:
    def __init__(self):
        with open('cv_info_extractor/resources/keywords.txt', 'r', encoding="utf-8") as file:
            self.keywords = [l.strip() for l in file.readlines()]

    def match_sections(self, inp):
        idxs = [{k:inp.find(k)} for k in self.keywords if inp.find(k) != -1]
        idxs.append({'END':len(inp)})
        idxs.sort(key=lambda x: list(x.values())[0])
        idx_vals = [list(i.values())[0] for i in idxs]
        matches = [{list(idxs[i].keys())[0]:inp[idx_vals[i] + len(list(idxs[i].keys())[0]) + 1:idx_vals[i+1]]} for i in range(len(idx_vals) - 1)]
        return matches

    def find_sections(self, text):
        matched_sections = self.match_sections(text)
        if not matched_sections:
            return 'Not Found'
        return matched_sections