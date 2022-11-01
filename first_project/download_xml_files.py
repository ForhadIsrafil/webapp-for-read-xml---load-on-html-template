import os
import time
import requests
from bs4 import BeautifulSoup as soup

try:
    os.mkdir("xml_files")
except Exception as e:
    pass
url = 'https://www.govinfo.gov/bulkdata/ECFR'
xml_addr = 'https://www.govinfo.gov/bulkdata/ECFR/title-50/ECFR-title50.xml'

xml_number = 1
while True:

    request = requests.get(f'https://www.govinfo.gov/bulkdata/ECFR/title-{xml_number}/ECFR-title{xml_number}.xml')
    print(f"ECFR-title{xml_number}.xml")

    if request.status_code == 200:
        with open(f"xml_files/ECFR-title{xml_number}.xml", "w+b") as xml_file:
            xml_file.write(request.content)
            xml_file.close()

        if xml_number == 2:
            break

        xml_number += 1
        time.sleep(4)

    else:
        print(f"ECFR-title{xml_number}.xml not found. Exitting.")
        break

'''
Het, Forhadisrafil, so I did end up going with a cheaper bid, 
but as we discovered the United States Code ("USC") can only be obtained by scraping the .gov website. 
The XML bulk data which I sent you a link for is for the Code of Federal Regulations ("CFR") which is different.

Since you have been really enthusiastic about the project (which I really apricate) I want to work with you 
as well doing the CFR.

Here is what I propose: we break up the project into a couple milestones. 
The first milestone will be to write a script (preferably in python) that will 
download the CFR xml files form the .gov website to an AWS thorough an ec2 instance. 
This script will automatically run upon bootup of the instance and will check the website once every 24 hours. 
The second milestone will be creating the endpoints of the site that have the CFR sections. 
The third milestone will be implementing the search functionality and the ability for users to navigate towards endpoints. The cost of these milestones can be divided in however you see fit.

https://www.law.cornell.edu/uscode/text
'''
