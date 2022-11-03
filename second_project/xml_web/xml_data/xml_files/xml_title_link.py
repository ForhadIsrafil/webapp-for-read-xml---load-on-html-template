import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
from glob import glob
from django.conf import settings
from pregex.core.groups import Capture
from pregex.core.classes import AnyDigit, AnyButWhitespace, AnyWhitespace, AnyFrom
from pregex.core.quantifiers import Exactly, Optional, OneOrMore, AtLeastAtMost


def get_links(title_number):
    link_data = []

    try:
        with open(os.path.join(os.path.join(os.path.dirname(__file__)), f"ECFR-title{title_number}.xml"), 'r',
                  encoding='utf8') as f:
            data = f.read()

        data = BeautifulSoup(data, "xml")

        # print(data.find_all("HEAD")[0].parent.attrs)
        #
        for title in data.find_all("HEAD"):
            print(title.parent.attrs)
            # print(title)
            temp_dict = title.parent.attrs
            temp_dict['title'] = title.text
            temp_dict['title_number'] = title_number
            link_data.append(temp_dict)
    except Exception as e:
        pass
    # print(link_data)
    return link_data


def get_exact_details(title_number, section_number):
    try:
        with open(os.path.join(os.path.join(os.path.dirname(__file__)), f"ECFR-title{title_number}.xml"), 'r',
                  encoding='utf8') as f:
            read_data = f.read()

        data = BeautifulSoup(read_data, "xml")
        exact_data = data.find_all(attrs={"N": f"{section_number}"})

        cita = BeautifulSoup(str(exact_data[0]), "xml")
        citation = cita.find(name="CITA")
        if citation != None:
            pattern = (OneOrMore(AnyDigit()) + OneOrMore(AnyWhitespace()) + Capture("FR" + AnyWhitespace()) + OneOrMore(
                AnyDigit()))
            citations = pattern.get_matches(citation.text)
            # print(citations)
        else:
            citations = []

        if exact_data != None:
            return " ".join(str(d) for d in exact_data), citations
        else:
            return '', []
    except Exception as e:
        print(e)
        return '', []


def title_list():
    title_arr = []
    titles = glob(os.path.join(os.path.join(os.path.dirname(__file__))) + "\*.xml")

    for title in titles:
        xml_file_name = title.split('\\')[-1]
        title_number = xml_file_name.split('title')[-1].replace(".xml", "").strip()
        print(title_number)

        try:
            with open(os.path.join(os.path.join(os.path.dirname(__file__)), xml_file_name), 'r', encoding='utf8') as f:
                data = f.read()

            data = BeautifulSoup(data, "xml")
            title_header = data.find_all("HEAD")[0:1][0]

            title_arr.append({"title_number": title_number, "title_header": title_header.text})
        except Exception as e:
            pass

    return title_arr


''''''
