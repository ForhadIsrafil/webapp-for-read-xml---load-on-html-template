import xmltodict
import json
import pandas as pd


def xml_dict_data(xml_file_path, id):
    file = open(xml_file_path, encoding="utf8")
    xml_att = xmltodict.parse(file.read())
    # print(xml_att, )

    with open(f"ECFR-title{id}.json", "w", ) as d:
        d.write(json.dumps(xml_att, ))


for i in range(1, 3):
    xml_dict_data(f"xml_files/ECFR-title{i}.xml", i)

'''
https://www.law.cornell.edu/uscode/text

Sounds great! And yes, so we want to create endpoints so that users can navigate to the regulation they want to view. 
Here is an example: https://www.law.cornell.edu/cfr/text

We start at the main page and then can navigate to a particular title (https://www.law.cornell.edu/cfr/text/3) and then 
chatper (https://www.law.cornell.edu/cfr/text/3/chapter-I), subchaters (if present),
sections (https://www.law.cornell.edu/cfr/text/3/part-100) [with the authority for the regulation], 
and then finally, to the actual regulation itself ( https://www.law.cornell.edu/cfr/text/3/100.1)


============
https://www.ecfr.gov/current/title-1
'''
