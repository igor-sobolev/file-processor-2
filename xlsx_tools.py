#from openpyxl import load_workbook
import pandas as pd
import json

def isNaN(x):
    return x != x

def parse_xlsx(operator, filename):
    data = pd.read_excel(filename, sheetname='Voice')
    parsed = { '__TYPE__': operator }
    subsection = 0
    print(len(data.values))
    for row in data.values:
        print(row, row[1])
        if not isNaN(row[1]) and not isNaN(row[2]):
            if subsection not in parsed:
                parsed[subsection] = { row[1]: row[2] }
            else:
                parsed[subsection][row[1]] = row[2]
        if not isNaN(row[1]) and isNaN(row[2]):
            subsection = row[1]
        if isNaN(row[1]) and isNaN(row[2]):
            continue
    print(json.dumps(parsed, indent = 2))
    return parsed

def parse_bundle(file_tuples):
    parsed = []
    for file in file_tuples:
        parsed.append(parse_xlsx(file[0], file[1]))
    for o in parsed:
        for section in o.keys():
            print('object!!!! ', json.dumps(o, indent = 2))
            print('section!!!! ', o[section])
            if (section == '__TYPE__'):
                continue
            for entry in o[section].keys():
                for o1 in parsed:
                    if entry not in o1[section]:
                        o1[section][entry] = None
    return parsed


#parse_xlsx('/home/igor/workspace/awtg/documents_all/2G-EE/Norfolk-2G-EE 140318.xlsx')