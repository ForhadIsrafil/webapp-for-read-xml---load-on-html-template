import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os

from django.conf import settings

print("ddddddd ", os.path.join(os.path.dirname(__file__)))


def get_links():
    with open(os.path.join(os.path.join(os.path.dirname(__file__)), "ECFR-title1.xml"), 'r', encoding='utf8') as f:
        data = f.read()

    data = BeautifulSoup(data, "xml")

    # print(data.find_all("HEAD")[0].parent.attrs)
    #
    link_data = []
    for title in data.find_all("HEAD")[0:20]:
        print(title.parent.attrs)
        print(title)
        temp_dict = title.parent.attrs
        temp_dict['title'] = title.text
        link_data.append(temp_dict)

    # print(link_data)
    return link_data


def get_exact_details(n):
    with open(os.path.join(os.path.join(os.path.dirname(__file__)), "ECFR-title1.xml"), 'r', encoding='utf8') as f:
        read_data = f.read()

    data = BeautifulSoup(read_data, "xml")
    exact_data = data.find(attrs={"N": f"{n}"})

    if exact_data != None:
        return exact_data
    else:
        return ''
