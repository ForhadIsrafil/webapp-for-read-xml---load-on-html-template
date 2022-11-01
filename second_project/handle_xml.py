import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# tree = ET.parse('xml_files/ECFR-title1.xml')
# root = tree.getroot()
#
#
# for main_child in root[1]:
#     for child in main_child1:
#         print(child)
with open('xml_files/ECFR-title1.xml', 'r', encoding='utf8') as f:
    read_data = f.read()

data = BeautifulSoup(read_data, "xml")

# print(data.find_all("HEAD")[0].parent.attrs)
#
link_data = []
for title in data.find_all("HEAD")[0:10]:
    print(title.parent.attrs)
    print(title)
    temp_dict = title.parent.attrs
    temp_dict['title'] = title.text
    link_data.append(temp_dict)
    # break
# print(data_dict)

print(data.find(attrs={"N": "§ 2.2"}))  # important

# for title in data.find_all("DIV8", {"N": "§ 5.10"}):
#     print(title.text.strip())


# for i in range(1,21):
#     for title in data.find_all(f"DIV{i}")[0:10]:
#         print(title)
#         break
#     break
