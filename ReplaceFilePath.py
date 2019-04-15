## This is a very basic Python script that renames the schemaLocation URL's within the XML Schema files
## I am doing this so I can properly validate the XSD file in http://www.utilities-online.info/xsdvalidation/#.XLS40egzaUl

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for file in os.listdir(dir_path):
    if file.endswith(".xsd"):
        with open(file) as f:
            newText=f.read().replace('"IMSpoor-', '"https://raw.githubusercontent.com/XanderdenDuijn/IMX/master/IMSpoor-')

        with open(file, "w") as f:
            f.write(newText)
        print("succesfully renamed ",file) 



          



