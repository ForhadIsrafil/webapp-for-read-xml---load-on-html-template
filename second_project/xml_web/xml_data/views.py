from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

from .xml_files.xml_title_link import get_links, get_exact_details, title_list


def get_list_of_titles(request):
    if request.method == "POST":
        title_number = request.POST.get("title_number")
        section_number = request.POST.get("section_number")
        if title_number != "" or section_number != "":
            return redirect("section_details", title_number, "§ " + section_number.strip())
        else:
            return redirect("list_of_titles")

    titles = title_list()
    context = {"titles": titles}
    return render(request, "list_of_titles.html", context)


def read_single_title(request, title_number):
    return render(request, 'xml_data.html', {"link_data": get_links(title_number), "title_number": title_number})


def section_details(request, title_number, section_number):
    if title_number != "" or section_number != "":
        context = {
            "details": get_exact_details(title_number, section_number),
            "section_number": f"Title {title_number}, {section_number}",
        }
        return render(request, 'xml_details_data.html', context)
    else:
        return redirect('/')


def search_title(request):
    print(request.POST)

    if request.method == "POST":
        title_number = request.POST.get("title_number")
        section_number = request.POST.get("section_number")
        if title_number != "" or section_number != "":
            context = {
                "details": get_exact_details(title_number, "§ " + section_number),
                "section_number": f"Title {title_number}, {section_number}",
            }
            return redirect("section_details", title_number=title_number, section_number=section_number)
    else:
        return redirect('/')
