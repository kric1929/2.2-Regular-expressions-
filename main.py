import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ

pattern_lfs = re.compile("'([А-Я][а-я]+) ([А-Я][а-я]+) ([А-Я][а-я]+)',(( '',){,2})")
pattern_l_fs = re.compile("'([А-Я][а-я]+)', '([А-Я][а-я]+) ([А-Я][а-я]+)',(( '',){,1})")
pattern_lf = re.compile("'([А-Я][а-я]+) ([А-Я][а-я]+)', '', '',")
pattern_phone = re.compile("(\+*)([0-9])([\s]*)(\(*)(\d{3})([\)\-]*)(\s*)(\d{3})([\-]*)(\d{2})([\-]*)(\d{2})(\S)")
pattern_phone_additional = re.compile(
    "(\+*)([0-9])([\s]*)(\(*)(\d{3})([\)\-]*)(\s*)(\d{3})([\-]*)(\d{2})([\-]*)(\d{2})(\s)(\(?)(\w*)(\D)(\s*)(\d*)(\)?)")
sub_pattern_lfs = r"'\1', '\2', '\3',"
sub_pattern_l_fs = r"'\1', '\2', '\3',"
sub_pattern_lf = r"'\1', '\2', '',"
sub_pattern_phone = r"+7(\5)\8-\10-\12"
sub_pattern_phone_additional = r"+7(\5)\8-\10-\12 доб.\18"

contacts_list_corrected = []

for contact in contacts_list:
    text_corrected = pattern_lfs.sub(sub_pattern_lfs, str(contact))
    text_corrected1 = pattern_l_fs.sub(sub_pattern_l_fs, text_corrected)
    text_corrected2 = pattern_lf.sub(sub_pattern_lf, text_corrected1)
    text_corrected3 = pattern_phone.sub(sub_pattern_phone, text_corrected2)
    text_corrected4 = pattern_phone_additional.sub(sub_pattern_phone_additional, text_corrected3)
    result_list = [element.strip("'[]") for element in text_corrected4.split(", ")]
    contacts_list_corrected.append(result_list)

contact_dict = {}

for contacts in contacts_list_corrected:
    name = f'{contacts[0]} {contacts[1]}'
    try:
        old_person = contact_dict[name]
        for k, v in enumerate(contacts):
            if not old_person[k]:
                old_person[k] = v
    except KeyError:
        contact_dict[name] = contacts

formatted_contact_list = []

for k, v in contact_dict.items():
    formatted_contact_list.append(v)


# TODO 2: сохраните получившиеся данные в другой файл

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(formatted_contact_list)
