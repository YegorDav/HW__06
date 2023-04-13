import shutil
import string


def normalize(name):

    tr_table = str.maketrans('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                             'abvgdeejzijklmnoprstufhccss_yeuy')
    name = name.translate(tr_table).lower()
    name = ''.join(c if c.isalnum() else '_' for c in name)
    return name
