#from openpyxl import load_workbook
import pandas as pd
import json
from collections import OrderedDict

def isNaN(x):
    return x != x

def parse_xlsx(operator, filename, sheet):
    print(filename, '\n', sheet)
    data = pd.read_excel(filename, sheet_name = sheet)
    parsed = OrderedDict([('__TYPE__', operator)])
    subsection = 0
    for row in data.values:
        if not isNaN(row[1]) and not isNaN(row[2]):
            if subsection not in parsed:
                parsed[subsection] = { row[1]: row[2] }
            else:
                parsed[subsection][row[1]] = row[2]
        if not isNaN(row[1]) and isNaN(row[2]):
            subsection = row[1]
        if isNaN(row[1]) and isNaN(row[2]):
            continue
    # print(json.dumps(parsed, indent = 2))
    return parsed

def parse_bundle(files, sheet):
    parsed = []
    for file in files:
        parsed.append(parse_xlsx(file['operator_short_name'], file['path'], sheet))
    for o in parsed:
        for section in o.keys():
            if (section == '__TYPE__'):
                continue
            for entry in o[section].keys():
                for o1 in parsed:
                    if entry not in o1[section]:
                        o1[section][entry] = 0
    return parsed


#parse_xlsx('/home/igor/workspace/awtg/documents_all/2G-EE/Norfolk-2G-EE 140318.xlsx')