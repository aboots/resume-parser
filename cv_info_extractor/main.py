from pprint import pprint

from PyPDF2 import PdfReader
from hazm import Normalizer

from cv_info_extractor.email_detector import EmailDetection
from cv_info_extractor.name_detector import NameDetection
from cv_info_extractor.phone_number_detector import PhoneNumberDetection
from cv_info_extractor.date_extractor import DateDetection
from cv_info_extractor.section_extractor import SectionExtractor
from utils import CusNormalizer


def run(address, output_file='output.txt'):
    final_text = ''
    reader = PdfReader(address)
    for page in reader.pages:
        text = page.extract_text()
        final_text += text
    email = EmailDetection().find_email(final_text)
    print(f"Email = {email}")
    normalizer = Normalizer()
    final_text = normalizer.normalize(final_text)
    final_text = CusNormalizer().normalize(final_text)
    print(final_text)
    full_name, first_name, last_name = NameDetection().find_name(final_text)
    print(f"Full Name = {full_name}")
    print(f"First Name = {first_name}")
    print(f"Last Name = {last_name}")
    phone_number = PhoneNumberDetection().find_phone_number(final_text)
    print(f'Phone Number = {phone_number}')
    date = DateDetection().find_date_number(final_text)
    print(f'Date = {date}')
    extra = SectionExtractor().find_sections(final_text)
    for item in extra:
        print('----------------')
        print(item)
