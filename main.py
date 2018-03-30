from guizero import App, PushButton, TextBox
from docx_tools import compose_docx

# def do_nothing():
#     print(int(a.value) + int(b.value))

# app = App(title="Keypad example", width=500, height=190, layout="grid")
# processButton = PushButton(app, command=do_nothing, text="Add", grid=[0,0])
# a = TextBox(app, text="0", grid=[1,1])
# b = TextBox(app, text="0", grid=[1,0])

# app.display()

files_to_compose = [
    ('ee', '/home/igor/workspace/awtg/documents_all/2G-EE/Norfolk-2G-EE 140318.xlsx'),
    ('ee', '/home/igor/workspace/awtg/documents_all/2G-EE/Norfolk-2G-EE 160318.xlsx')
]

compose_docx('demo1.docx', files_to_compose)
