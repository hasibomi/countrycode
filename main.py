import os

from converter import Converter


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    converter = Converter(os.path.join(BASE_DIR, 'list.json'), "country_codes")
    converter.convert()