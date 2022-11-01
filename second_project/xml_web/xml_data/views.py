from django.conf import settings
from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from .xml_files.xml_title_link import get_links, get_exact_details


def read_xml(request):
    # with open('xml_files/ECFR-title2.xml', 'r', encoding='utf8') as f:
    #     data = f.read()
    #
    # data = BeautifulSoup(data, "xml")
    #
    # # print(data.find_all("HEAD")[0].parent.attrs)
    # #
    # link_data = []
    # for title in data.find_all("HEAD")[0:10]:
    #     print(title.parent.attrs)
    #     print(title)
    #     temp_dict = title.parent.attrs
    #     temp_dict['title'] = title.text
    #     link_data.append(temp_dict)
    #     # break
    # # print(link_data)
    return render(request, 'xml_data_demo.html', {"link_data": get_links()})

def get_details(request, n):
    if n != "":
        context = {
            "details": get_exact_details(n)
        }
        return render(request, 'xml_details_data.html', context)
    else:
        return redirect('/')