from docx import Document
import xlsx_tools
from docx.shared import Inches

def compose_docx(target_name, excels_to_parse):
    document = Document()

    #document.add_heading('Draft', 0)

    # p = document.add_paragraph('A plain paragraph having some ')
    # p.add_run('bold').bold = True
    # p.add_run(' and some ')
    # p.add_run('italic.').italic = True

    # document.add_heading('Heading, level 1', level=1)
    # document.add_paragraph('Intense quote', style='IntenseQuote')

    # document.add_paragraph('first item in unordered list', style='ListBullet')
    # document.add_paragraph('first item in ordered list', style='ListNumber')

    # document.add_picture('./xl/media/image4.png', width=Inches(1.25))
    # document.add_picture('./xl/media/image6.png', width=Inches(1.25))

    # PARSING FILE BUNDLE
    parsed = xlsx_tools.parse_bundle(excels_to_parse)

    table = document.add_table(rows = 0, cols = len(parsed) + 1)
    for section in parsed[0].keys():
        row_cells = table.add_row().cells
        row_cells[0].text = str(section)
        if isinstance(parsed[0][section], str):
            continue
        for entry in parsed[0][section].keys():
            entries_row_cells = table.add_row().cells
            for index, operator in enumerate(parsed):
                entries_row_cells[index + 1].text = str(operator[section][entry])


    document.add_page_break()

    document.save(target_name)

#compose_docx('./demo1.docx')
