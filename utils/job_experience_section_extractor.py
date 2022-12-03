from cv_info_extractor.section_extractor import SectionExtractor


class JobExpSecExtraction:
    def __init__(self):
        self.keyword = SectionExtractor().keywords[0][0]

    def extract(self, sections):
        if self.keyword not in sections:
            return 'Not Found'
        return sections[self.keyword]
