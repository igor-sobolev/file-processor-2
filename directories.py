import os
import re
import json

FILE_PATTERN = r'.*?\/*(\w+)-(\w+)[-\s]*(\w+)*-(\w+)[-\s]*(\d{6})(.*)(.xlsx)';

def find_files(path):
    excels = [os.path.join(root, name)
        for root, dirs, files in os.walk(path)
        for name in files
        if name.endswith(('.xls', '.xlsx')) and not name.startswith(('.', '$', '~'))]
    excels_by_tech = {}
    for excel in excels:
        results = re.match(FILE_PATTERN, excel[len(path):])
        if results:
            technology = results.group(2).lower()
            test_type = results.group(3).lower() if results.group(3) else ''
            combined_tech = technology + '-' + test_type if test_type else technology
            test_date = results.group(5).lower()

            excel_info = {}
            excel_info['place'] = results.group(1).lower()
            excel_info['technology'] = technology
            excel_info['test_type'] = test_type
            excel_info['operator_short_name'] = results.group(4).lower()
            excel_info['test_date'] = test_date
            excel_info['comment'] = results.group(6)
            excel_info['path'] = excel
            if combined_tech not in excels_by_tech:
                excels_by_tech[combined_tech] = {}
            if test_date not in excels_by_tech[combined_tech]:
                excels_by_tech[combined_tech][test_date] = []
            excels_by_tech[combined_tech][test_date].append(excel_info)

    # print(json.dumps(excels_by_tech, indent = 2))
    return excels_by_tech

#find_files('/home/igor/workspace/awtg/documents_all/')
