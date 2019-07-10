## This is a very basic Python script that renames the schemaLocation URL's within the XML Schema files
## I am doing this so I can properly validate the XSD file in http://www.utilities-online.info/xsdvalidation/#.XLS40egzaUl
## Note that this validation method will only work when the IMX repository is a public one

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(dir_path):
    if file.endswith(".xsd"):
        with open(file, encoding="utf8") as f:
            newText=f.read().replace('"IMSpoor-', '"https://raw.githubusercontent.com/XanderdenDuijn/IMX/master/IMSpoor-')

        with open(file, "w", encoding="utf8") as f:
            f.write(newText)
        print("succesfully renamed ",file) 



          



