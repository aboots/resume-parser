from PyPDF2 import PdfReader
from hazm import Normalizer
import re

from cv_info_extractor.city_extractor import CityProvinceExtractor
from cv_info_extractor.email_detector import EmailDetection
from cv_info_extractor.name_detector import NameDetection
from cv_info_extractor.phone_number_detector import PhoneNumberDetection
from cv_info_extractor.date_extractor import DateDetection
from cv_info_extractor.section_extractor import SectionExtractor
from utils import CusNormalizer


def run(address):
    final_text = ''
    result = {}
    reader = PdfReader(address)
    for page in reader.pages:
        text = page.extract_text()
        final_text += text
    email = EmailDetection().find_email(final_text)
    normalizer = Normalizer()
    # final_text = normalizer.normalize(final_text)

    final_text = CusNormalizer().normalize(final_text)
    print(final_text)
    result['ایمیل'] = email
    full_name, first_name, last_name = NameDetection().find_name(final_text)
    result['نام'] = first_name
    result['نام خانوادگی'] = last_name
    phone_number = PhoneNumberDetection().find_phone_number(final_text)
    result['شماره تماس'] = phone_number
    print(phone_number)
    date = DateDetection().find_date_number(final_text)
    result['تاریخ تولد'] = date
    city = CityProvinceExtractor().find(final_text)[0]
    result['استان محل سکونت'] = city['province']
    result['شهر محل سکونت'] = city['city']
    extra = SectionExtractor().find_sections(final_text)
    for info in extra:
        if type(info) == dict:
            result.update(info)
    print(result)
    return result
